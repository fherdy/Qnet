<template>
  <div class="header mt-3">
    <router-link class="bar-logo" tag="a" to="/">
      <img src="@/assets/logo.png" alt="Qnet_Logo" />
    </router-link>
		<div class="navbar">
      <router-link tag="a" to="/">
        Home
      </router-link>
      <router-link tag="a" to="/about">
        About
      </router-link>
      <router-link tag="a" to="/contact">
        Contact
      </router-link>
		</div>
  </div>
</template>

<script>
export default {
  name: 'Navigation',
  data() {
    return {
    };
  },
};
</script>

<style lang="scss" scoped>
.header {
  width: 100%;
  max-width: 600px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  .bar-logo > img {
    width: 200px;
    height: 200px;
  }

  .navbar {
    width: 100%;
    max-width: 300px;
  }
}

// .autocomplete-items {
//   position: absolute;
//   border: 1px solid #d4d4d4;
//   border-bottom: none;
//   border-top: none;
//   z-index: 99;
//   top: 100%;
//   left: 0;
//   right: 0;
// }

// .autocomplete-items div {
//   padding: 10px;
//   cursor: pointer;
//   background-color: #fff;
//   border-bottom: 1px solid #d4d4d4;
// }


// .autocomplete-items div:hover {
//   background-color: #e9e9e9;
// }


// .autocomplete-active {
//   background-color: DodgerBlue !important;
//   color: #ffffff;
// }

</style>
