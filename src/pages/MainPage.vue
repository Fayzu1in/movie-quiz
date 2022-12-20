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
          <div class="score">
            {{ score }}<img src="@/assets/img/star.png" alt="" />
          </div>
        </div>
        <!-- <button class="about__right-bottom" @click="$router.push('/play')">
          Начать игру
        </button> -->
        <router-link
          @click="countDownTimer()"
          :to="{ path: '/play' }"
          class="about__right-bottom"
        >
          Начать игру</router-link
        >
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
import { mapState } from "pinia";
import SubscribeCard from "../components/SubscribeCard.vue";
import { useQuizStore } from "../store";
// const store = useStore;
export default {
  components: {
    SubscribeCard,
  },
  data() {
    return {
      subscribes: [
        {
          name: "Four in play",
          period: "1 день",
          price: 27,
        },
        {
          name: "Four in play",
          period: "3 дня",
          price: 79,
        },
        {
          name: "Four in play",
          period: "7 дней",
          price: 180,
        },
      ],
    };
  },
  computed: {
    ...mapState(useQuizStore, ["score"]),
  },
  mounted() {
    console.log(this.score);
  },
  // provide() {
  //   return {
  //     countDown: this.countDown,
  //     timer: this.timer,
  //   };
  // },
  provide: {
    countDown: "countDown",
    timer: "timer",
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
  @media only screen and (max-width: 420px) {
    margin-top: 0px;
  }
  &__img {
    height: 72px;
    border-radius: 50%;
    margin-right: 24px;
    @media only screen and (max-width: 420px) {
      height: 40px;
      margin-right: 10px;
    }
  }
  &__name {
    color: #fff;
    font-size: 64px;
    padding-right: 20px;
    @media only screen and (max-width: 420px) {
      font-size: 22px;

      padding-right: 10px;
    }
  }
}
.about {
  display: flex;
  justify-content: space-between;
  align-items: center;
  @media only screen and (max-width: 420px) {
    flex-direction: column;
  }
  &__left {
    &-top {
      font-size: 54px;
      font-weight: 500;
      padding-top: 16px;
      padding-bottom: 16px;
      @media only screen and (max-width: 420px) {
        font-size: 22px;
        padding-bottom: 7px;
      }
      .gameName {
        padding-right: 8px;
        @media only screen and (max-width: 420px) {
          padding-right: 4px;
        }
      }
      .gameName2 {
        color: #ff9900;
        @media only screen and (max-width: 420px) {
        }
      }
    }
    &-bottom {
      max-width: 500px;
      width: 100%;
      font-size: 18px;
      color: #9b9b9a;
      @media only screen and (max-width: 420px) {
        max-width: 340px;
        width: 100%;
        font-size: 16px;
      }
    }
  }
  &__right {
    max-width: 495px;
    width: 100%;
    display: flex;
    flex-direction: column;
    @media only screen and (max-width: 420px) {
      // max-width: 320px;
      // width: 100%;
    }
    &-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 22px;
      border-bottom: 1px solid rgb(49, 49, 52);
      padding-bottom: 16px;
      @media only screen and (max-width: 420px) {
        font-size: 18px;
        margin-top: 30px;
      }
      .scoreText {
        color: #9b9b9a;
      }
      .score {
        display: flex;
        // align-items: flex-end;
        @media only screen and (max-width: 420px) {
        }
        img {
          padding-left: 15px;
          margin-top: -5px;
          @media only screen and (max-width: 420px) {
            height: 25px;
            margin-top: -3px;
            padding-left: 7px;
          }
        }
      }
    }
    &-bottom {
      text-transform: uppercase;
      background: #383838;
      color: #fff;
      border: 3px solid transparent;
      border-radius: 4px;
      font-size: 22px;
      padding-top: 10px;
      padding-bottom: 10px;
      margin-top: 16px;
      text-align: center;
      text-decoration: none;
      cursor: pointer;
      @media only screen and (max-width: 420px) {
        cursor: unset;
        font-size: 18px;
      }
      &:hover {
        border: 3px solid #ff9900;
        @media only screen and (max-width: 420px) {
          border: unset;
        }
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
  padding-bottom: 74px;
  @media only screen and (max-width: 420px) {
    font-size: 22px;
    max-width: 320px;
    width: 100%;
    padding-top: 30px;
    padding-bottom: 30px;
  }
}
.subscribes {
  display: flex;
  justify-content: space-between;
  padding-bottom: 50px;

  @media only screen and (max-width: 420px) {
    flex-direction: column;
    padding-bottom: 30px;
    align-items: center;
  }
}
</style>
