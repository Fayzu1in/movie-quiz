<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
// import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",
  components: {
    // HelloWorld,
    NavBar,
  },
};
</script>

<style lang="scss">
* {
  box-sizing: border-box;
}
html {
  background: black;
  font-family: sans-serif;
  color: #fff;
}
.container {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}
</style>
