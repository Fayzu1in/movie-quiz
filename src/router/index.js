import VueRouter from "vue-router";
import MainPage from "../pages/MainPage";
import GamePlay from "../pages/GamePlay";
export default new VueRouter({
  routes: [
    {
      path: "/",
      component: MainPage,
    },
    {
      path: "/play",
      component: GamePlay,
    },
  ],
});
