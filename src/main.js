import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import router from "./router/index";
Vue.config.productionTip = false;
// import BootstrapVue from "bootstrap-vue";
// import BootstrapVue from "bootstrap-vue/dist/bootstrap-vue.esm";

// import "bootstrap/dist/css/bootstrap.css";
// import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(VueRouter);
// BootstrapVue
new Vue({
  render: (h) => h(App),
  el: "#app",
  router,
}).$mount("#app");
