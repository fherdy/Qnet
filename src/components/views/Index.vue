<template>
  <div class="index">
    <div class="mb-5 search-container">
      <search-bar
        placeholder="search school"
        :options="schools"
        @update="pickedSchool = $event"
        id="schoolsBar" class="mb-1"/>
      <search-bar
        placeholder="search course"
        :options="courses"
        @update="pickedCourse = $event"
        id="courseBar" class="mb-1"/>

      <div class="btn-bar">
        <div class="mr-auto">
          {{ this.pickedSchool }}
        </div>
        <div class="mr-auto">
          {{ this.pickedCourse }}
        </div>
			  <img :class="{'disabled' : !(this.pickedCourse && this.pickedSchool)}" src="@/assets/search-icon.svg" @click="submitSearch()">
      </div>
    </div>


    <div class="text mb-3" v-if="!dirty">
      <kbd>
        Find all your class quiz and test questions here.....
      </kbd>
    </div>
    <div class="question-box" v-else>
      <div v-if="filteredQuestions.length !== 0">
        <div v-for="(q,idx) in filteredQuestions" :key="idx" class="question mb-1">
          <div class="index">{{ idx + 1 }}.</div>
          <div class="text">{{ q.text }}</div>
        </div>
      </div>
      <div v-else>
        no questions found
      </div>
      <textarea v-model="questionInput" class="mt-5" />
      <div @click="addQuestion" class="add-question mb-5">
        add question
      </div>
    </div>

    <div class="pop" v-if="showModal">
      <div class="panel">
        <div class="mb-2">Confirmtion</div>
        <div class="ml-1 small-text mb-1" v-if="!schools.find(c => pickedSchool === c)">
          Adding new school
          <div class="ml-3">{{ this.pickedSchool }}</div>
        </div>
        <div class="ml-1 small-text mb-1" v-if="!courses.find(c => pickedCourse === c)">
          Adding new course
          <div class="ml-3">{{ this.pickedCourse }}</div>
        </div>
        <div class="btn-bar mt-5">
          <div @click="showModal = false" class="btn-cancel mr-5">
            cancel
          </div>
          <div @click="confirmedSearch()" class="btn-submit">
            submit
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar';

export default {
  name: 'Index',
  data() {
    return {
      schools: [],
      courses: [],
      questions: [],
      filteredQuestions: [],
      pickedSchool: null,
      pickedCourse: null,
      showModal: false,
      dirty: false,
      questionInput: '',
    };
  },
  components: {
    SearchBar,
  },
  mounted() {
    // 'http://10.255.139.136:5000'
    this.reloadInfo()
  },
  methods: {
    reloadInfo() {
      let baseurl = 'http://localhost:5000'
      this.axios.get(`${baseurl}/readInSchools`).then((response) => {
        this.schools = response.data
      })
      this.axios.get(`${baseurl}/readInCourses`).then((response) => {
        this.courses = response.data
      })
      this.axios.get(`${baseurl}/readInQuestions`).then((response) => {
        this.questions = response.data
      })
    },
    submitSearch() {
      if (this.pickedSchool && this.pickedCourse) {
        let foundSchool = this.schools.find(s => this.pickedSchool === s)
        let foundCourses = this.courses.find(c => this.pickedCourse === c)
        // alert(`${foundSchool},${foundCourses}`);
        console.log(foundSchool, foundCourses)
        if (!foundSchool || !foundCourses) {
          this.showModal = true
        } else {
          this.confirmedSearch()
        }
      }

    },
    confirmedSearch() {
      this.showModal = false;
      this.dirty = true;
      this.filteredQuestions = this.questions.filter(q => {
        return q.school === this.pickedSchool &&
          q.course === this.pickedCourse
      })
    },
    addQuestion() {
      let baseurl = 'http://localhost:5000'
      if (this.questionInput && this.questionInput !== '') {
        let inputstr = this.questionInput
        this.questionInput = ''
        this.axios.get(`${baseurl}/writeToQuestions?text=${encodeURIComponent(inputstr)}&school=${encodeURIComponent(this.pickedSchool)}&course=${encodeURIComponent(this.pickedCourse)}`).then((response) => {
          setTimeout(() => {
            this.reloadInfo()
            setTimeout(() => {
              this.confirmedSearch()
            }, 500);
          }, 500);
        })
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.index {
  .search-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;

    > input {
      width: 100%;
      height: 100%;
    }

    .btn-bar {
      width: 100%;
      display: flex;
      justify-content: flex-end;
      align-items: flex-end;
      > img {
        cursor: pointer;
        width: 60px;
        height: 20px;
        // height: 100%;
        background-color: darkorange;
        border-radius: 5px;
        transition: all 0.3s;
        &.disabled {
          filter: contrast(50%);
          cursor: disabled;
          pointer-events: none;
        }
        &:hover {
          filter: contrast(120%);
        }
      }
    }

    .text {
      kbd {
        width: 100%;
      }
    }
  }

  .question-box {
    .question {
      border-radius: 3px;
      position: relative;
      background-color: lightsteelblue;
      .index {
        position: absolute;
        top: 0px;
        left: 5px;
      }
      .text {
        padding-left: 25px;
      }
      textarea {
        width: 100%;
      }
    }
    .add-question {
      cursor: pointer;
      margin: 0 auto;
      background-color: green;
      color: white;
      width: 100px;
      border-radius: 3px;
      &:hover {
        background-color: darkgreen;
      }
    }
  }

  .pop {
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #000000aa;
    display: flex;
    justify-content: center;
    align-items: center;
    .panel {
      padding: 13px;
      text-align: left;
      background-color: white;
      border-radius: 3px;
      box-shadow: 1px 1px 3px 0px black;
      width: 300px;

      .small-text {
        font-size: 12px;
        &>div {
          font-size: 10px;
        }
      }

      .btn-bar {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        color: #ffeeff;
        .btn-submit {
          color: white;
          font-size: 14px;
          font-weight: 100;
          padding: 3px;
          background-color: green;
          border-radius: 3px;

          cursor: pointer;
        }
        .btn-cancel {
          color: white;
          font-size: 14px;
          font-weight: 100;
          padding: 3px;
          background-color: gray;
          border-radius: 3px;

          cursor: pointer;
        }
      }
    }
  }
}
</style>
