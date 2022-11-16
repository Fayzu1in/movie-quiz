import VueRouter from "vue-router";
import MainPage from "../pages/MainPage";

export default new VueRouter({
  routes: [
    {
      path: "/",
      component: MainPage,
    },
  ],
});
