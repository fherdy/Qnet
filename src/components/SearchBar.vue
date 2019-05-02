<template>
  <div class="search-bar mb-1">
    <input
      @focus="enableSuggestions()"
      @blur="disableSuggestions()"
      type="text"
      v-model="text"
      :placeholder="placeholder"
      >
    <div class="list" @mouseleave="unpick()" v-show="showSuggestions">
      <div
        class="list-item"
        @mouseover="picked(o)"
        v-for="(o, idx) in filtered" :key="idx">
        {{o}}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      showSuggestions: false,
      text: '',
      tmptext: null,
    };
  },
  props: {
    options: {
      type: Array,
      required: true,
    },
    placeholder: {
      type: String,
      required: true,
    },
  },
  mounted() {
  },
  computed: {
    filtered() {
      return this.options.filter(o => {
        return o.toLowerCase().includes(this.text.toLowerCase());
      })
    },
  },
  watch: {
    text() {
      this.tmptext = null
      this.$emit('update', this.text)
    }
  },
  methods: {
    disableSuggestions() {
      this.showSuggestions = false;
      // console.log('hide')
      if (this.tmptext != null && this.tmptext !== '') {
        this.text = this.tmptext
      }
    },
    enableSuggestions() {
      this.tmptext = null
      this.showSuggestions = true;
      // console.log('show')
    },
    picked(text) {
      // console.log(text)
      this.tmptext = text;
    },
    unpick() {
      this.tmptext = null
      // console.log('unpick')
    }
  },
};
</script>

<style lang="scss" scoped>
.search-bar {


  position: relative;
  width: 100%;
  input {
    width: 100%;
  }
  .list {
    overflow-y: scroll;
    max-height: 100px;
    height: auto;
    width: 100%;
    position: absolute;
    z-index: 1;
    background-color: white;
    box-shadow: 1px 1px 1px 1px #888888;
    .list-item {
      cursor: pointer;
    }
    > .list-item:hover {
      background-color: rgb(101,214,209);
    }
  }
}
</style>
