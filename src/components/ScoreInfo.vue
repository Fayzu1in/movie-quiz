<template>
  <div class="container">
    <div class="infoCard">
      <div class="info">
        <div class="info__title">Игра окончена</div>
        <div class="info__subtitle">Вы набрали:</div>
        <div class="info__score">
          {{ score }}<img src="@/assets/img/star.png" alt="" />
        </div>
        <!-- <button class="mainPageBtn">Главная</button> -->
        <router-link :to="{ path: '/' }" class="mainPageBtn"
          >Главная</router-link
        >
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from "pinia";
import { useQuizStore } from "../store";

export default {
  computed: {
    ...mapState(useQuizStore, ["score"]),
  },
};
</script>
<style lang="scss" scoped>
.infoCard {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  height: 100%;
  align-items: center;
}
.info {
  width: 600px;
  border: 3px solid #ff9900;
  color: #fff;
  text-align: center;
  // margin: 0 auto;
  padding: 30px 0;

  &__title {
    font-size: 32px;

    padding-bottom: 30px;
  }
  &__subtitle {
    font-size: 24px;

    padding-bottom: 30px;
  }
  &__score {
    font-size: 36px;
    font-weight: 600;
    padding-bottom: 30px;
    img {
      margin-left: 10px;
    }
  }
  .mainPageBtn {
    background-color: #ff9900;
    color: #fff;
    text-decoration: none;
    padding: 5px 60px;
    font-size: 22px;
  }
}
</style>
