<template>
  <div>
    <div class="container gameSection">
      <div class="gamePlay">
        <div class="scoreInfo">
          <div class="scoreInfo__name">User Name</div>
          <div class="scoreInfo__score">
            {{ score }}
            <img src="@/assets/img/star.png" alt="" />
          </div>
          <button @click="startQuiz = !startQuiz" class="scoreInfo__endGameBtn">
            Завершить
          </button>
        </div>
      </div>
    </div>
    <div class="quizCard container">
      <quiz-start
        v-on:quizStartValue="QuizValue($event)"
        v-on:quizEndValue="quizEndValue($event)"
        v-if="startQuiz"
      ></quiz-start>
      <score-info v-if="quizEnd"></score-info>
    </div>
  </div>
</template>
<script>
import QuizStart from "../components/QuizStart.vue";
import ScoreInfo from "../components/ScoreInfo.vue";
import { useQuizStore } from "../store";
import { mapState } from "pinia";

export default {
  components: {
    QuizStart,
    ScoreInfo,
  },
  data() {
    return {
      startQuiz: true,
      quizEnd: false,
    };
  },
  // inject: ["score"],
  methods: {
    // startQuizFunc() {},
    QuizValue: function (QuizValue) {
      this.startQuiz = QuizValue;
    },
    quizEndValue: function (quizEndValue) {
      this.quizEnd = quizEndValue;
    },
  },
  mounted() {
    console.log(this.score);
    console.log(this.startQuiz);
    console.log(this.quizEnd);
  },
  computed: {
    ...mapState(useQuizStore, ["score"]),
  },
};
</script>
<style lang="scss">
.quizCard {
  display: flex;
  justify-content: center;
  // flex-direction: column;
}
.gameSection {
  display: flex;
  justify-content: flex-end;
}
.gamePlay {
  display: flex;
  flex-direction: column;
}
.scoreInfo {
  float: right;
  font-size: 22px;
  text-align: right;
  &__name {
    border-bottom: 1px solid rgb(49, 49, 52);
    padding-bottom: 13px;
  }
  &__score {
    border-bottom: 1px solid rgb(49, 49, 52);
    padding-bottom: 13px;
    padding-top: 13px;
    // display: flex;
    // justify-content: flex-end;
    // align-items: center;
    img {
      height: 26px;
      margin-bottom: -3px;
      padding-left: 10px;
    }
  }
  &__endGameBtn {
    background: red;
    color: white;
    border: none;
    font-size: 18px;
    padding: 4px 50px;
    cursor: pointer;
    margin-top: 13px;
  }
}
</style>
