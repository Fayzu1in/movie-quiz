<template>
  <div>
    <div class="container">
      <div class="profileInfo">
        <img class="profileInfo__img" src="@/assets/img/profile.jpg" alt="" />
        <span class="profileInfo__name">Rick Sanchez</span>
      </div>
    </div>
    <div class="container about">
      <div class="about__left">
        <div class="about__left-top">
          <span class="gameName">QUIZ</span>
          <span class="gameName2">GAME</span>
        </div>
        <div class="about__left-bottom">
          Играй и выигрывай подписки вместе c нашей новой игрой Allplay Quiz
          Game. Ну что Солдат, всё что тебе нужно, это отгадать фильм по кадру и
          набрать определенное количество баллов. Удачи!
        </div>
      </div>
      <div class="about__right">
        <div class="about__right-top">
          <div class="scoreText">SCORE:</div>
          <div class="score">0<img src="@/assets/img/star.png" alt="" /></div>
        </div>
        <button class="about__right-bottom">Начать игру</button>
      </div>
    </div>
    <div class="title container">
      Зарабатывай баллы и обменивай их на подписки!
    </div>
    <!-- <div class="subscribes container">

    </div> -->
    <div class="subscribes container">
      <subscribe-card
        v-for="(subscribe, index) in subscribes"
        :key="index"
        :name="subscribe.name"
        :period="subscribe.period"
        :price="subscribe.price"
      ></subscribe-card>
    </div>
  </div>
</template>
<script>
import SubscribeCard from "../components/SubscribeCard.vue";

export default {
  components: {
    SubscribeCard,
  },
  data() {
    return {
      subscribes: [
        {
          name: "Four in play",
          period: 1,
          price: 30,
        },
        {
          name: "Four in play",
          period: 3,
          price: 30,
        },
        {
          name: "Four in play",
          period: 7,
          price: 30,
        },
      ],
    };
  },
};
</script>
<style lang="scss" scoped>
.profileInfo {
  display: flex;
  align-items: center;
  border-bottom: 1px solid rgb(49, 49, 52);
  width: fit-content;
  padding-bottom: 16px;
  margin-top: 54px;
  &__img {
    height: 72px;
    border-radius: 50%;
    margin-right: 24px;
  }
  &__name {
    color: #fff;
    font-size: 64px;
    padding-right: 20px;
  }
}
.about {
  display: flex;
  justify-content: space-between;
  align-items: center;
  &__left {
    &-top {
      font-size: 54px;
      font-weight: 500;
      padding-top: 16px;
      padding-bottom: 16px;
      .gameName {
        padding-right: 8px;
      }
      .gameName2 {
        color: #ff9900;
      }
    }
    &-bottom {
      max-width: 500px;
      width: 100%;
      font-size: 18px;
      color: #9b9b9a;
    }
  }
  &__right {
    max-width: 495px;
    width: 100%;
    display: flex;
    flex-direction: column;
    &-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 22px;
      border-bottom: 1px solid rgb(49, 49, 52);
      padding-bottom: 16px;
      .scoreText {
        color: #9b9b9a;
      }
      .score {
        display: flex;
        // align-items: flex-end;
        img {
          padding-left: 15px;
          margin-top: -5px;
        }
      }
    }
    &-bottom {
      text-transform: uppercase;
      background: #383838;
      color: #fff;
      border: 2px solid transparent;
      border-radius: 4px;
      font-size: 22px;
      padding-top: 10px;
      padding-bottom: 10px;
      margin-top: 16px;
      cursor: pointer;
      &:hover {
        border: 2px solid #ff9900;
      }
    }
  }
}
.title {
  font-size: 40px;
  max-width: 700px;
  width: 100%;
  text-align: center;
  padding-top: 74px;
}
.subscribes {
  display: flex;
  justify-content: space-between;
}
</style>
