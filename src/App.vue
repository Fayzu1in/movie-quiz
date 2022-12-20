<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
    <!-- <button @click="data()">Data</button> -->
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
  // provide() {
  //   return { score: this.score };
  // },
  data() {
    return {
      showScore: false,
      // score: 0,
      startQuiz: false,
      // data: '{{data}}'
    };
  },
  methods: {
    data() {},
  },
};
</script>

<style lang="scss">
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}
html {
  background: black;
}
#app {
  background: black;
  font-family: sans-serif;
  color: #fff;
}

.container {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  @media only screen and (max-width: 420px) {
    max-width: 340px;
    width: 100%;
  }
}
</style>
