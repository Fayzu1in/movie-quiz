<template>
  <div>
    <div class="quiz">
      <div class="quiz__info">
        <div class="health">
          <img
            v-for="i in health"
            :key="i"
            src="@/assets/img/heart.png"
            class="heart"
          />
        </div>
        <div class="numberOfQuestion">
          {{ currentQuestion + 1 }}/{{ questionsAmount }}
        </div>
        <div class="time">{{ countDown }}s</div>
      </div>
      <div
        class="quiz__progress"
        id="myBar"
        :key="currentQuestion"
        :style="{
          width: progressWidth + '%',
        }"
      ></div>

      <div class="quiz__frame">
        <div v-if="incorrect" class="incorrect">
          <!-- <img class="incorrect__close" src="/close.png" alt="" /> -->
          <div class="incorrect__title">
            Упс. Ты не угадал <br />
            Верный ответ: <br />
            <p class="incorrect__title-answertxt">
              "{{
                questions[currentQuestion].answerOptions.find(
                  (i) => i.isCorrect === true
                ).answerText
              }}"
            </p>
          </div>

          <p class="incorrect__nextQuestionBtn" @click="nextQuestion()">
            Продолжить
          </p>
        </div>

        <div v-if="this.endGameWarningBtn" class="warning">
          <img
            class="warning__close"
            @click="warningClose()"
            src="/close.png"
            alt=""
          />
          <div class="warning__title">
            При завершении игры набранные баллы будут потеряны
          </div>

          <router-link class="endBtnLink" :to="{ path: '/' }">
            <p class="warning__endBtn" @click="endGame()">Завершить</p>
          </router-link>
        </div>
        <img :src="questions[currentQuestion].questionImage" alt="" />
      </div>
      <div v-if="!this.endGameWarningBtn" class="answersSection">
        <div class="showAnswers" v-if="this.showAnswers">
          <button
            :key="index"
            v-for="(option, index) in questions[currentQuestion].answerOptions"
            class="answerBtn"
            @click="answerClick(option.isCorrect)"
          >
            {{ option.answerText }}
          </button>
        </div>
        <!-- {{ this.endGameBtn }} -->
      </div>
    </div>
  </div>
</template>
<script>
import { useQuizStore } from "../store";
import { mapStores } from "pinia";
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

// Чтобы изменить значение переменной в store,
// необходимо в компоненте где будет даваться новое значение
// прописать import { mapStores } from "pinia";
// затем в computed прописать ...mapStores(названи стора),
// и затем в функции где будет даватться новое значение, с помощью
// this. назвние сторра и + к нему добавляем окончаниее Store(обязательно)
// пример ниже this.quizStore.score += 3;
//

export default {
  components: {},
  // inject: ["countDown", "timer"],
  // inject: ["score"],
  props: ["endGameWarningBtn"],
  data() {
    return {
      quizEnd: false,
      currentQuestion: 0,
      // progressWidth: 100,
      countDown: 10,
      timer: null,
      questionsAmount: 0,
      health: 3,
      startQuiz: true,
      endWarningValue: null,
      incorrect: false,
      showAnswers: true,
      questions: [
        {
          questionImage: "/hollywood.jpg",
          answerOptions: [
            { answerText: "Мачо и ботан", isCorrect: true },
            { answerText: "Шаг вперед", isCorrect: false },
            { answerText: "Дорогой Джон", isCorrect: false },
            { answerText: "Штурм белого дома", isCorrect: false },
          ],
        },
        {
          questionImage: "/anna.jpeg",
          answerOptions: [
            { answerText: "test 2", isCorrect: false },
            { answerText: "test 2", isCorrect: false },
            { answerText: "test 2", isCorrect: false },
            { answerText: "Бегущий по лезвию 2049", isCorrect: true },
          ],
        },
        {
          questionImage: "/jake.jpeg",
          answerOptions: [
            { answerText: "NightCrawler", isCorrect: true },
            { answerText: "test 3", isCorrect: false },
            { answerText: "test 3", isCorrect: false },
            { answerText: "test 3", isCorrect: false },
          ],
        },
        {
          questionImage: "/interstellar.jpeg",
          answerOptions: [
            { answerText: "Interstellar", isCorrect: true },
            { answerText: "test 4", isCorrect: false },
            { answerText: "test 4", isCorrect: false },
            { answerText: "test 4", isCorrect: false },
          ],
        },
      ],
    };
  },
  computed: {
    ...mapStores(useQuizStore),
    progressWidth() {
      return this.countDown * 10;
    },
  },

  methods: {
    endGame() {
      confirm("r u sure?");
      this.quizStore.score = 0;
    },

    warningClose() {
      this.endWarningValue = false;
      this.$emit("endWarningValue", this.endWarningValue);
    },

    countDownTimer() {
      if (this.countDown > -1) {
        this.timer = setTimeout(() => {
          this.countDown -= 1;
          // this.progressWidth -= 10;
          this.countDownTimer();
        }, 100000);
      } else if (this.questions.length - 1 == this.currentQuestion) {
        this.startQuiz = false;
        this.$emit("quizStartValue", this.startQuiz);
        this.quizEnd = true;
        this.$emit("quizEndValue", this.quizEnd);
      } else if (this.health === 0) {
        this.startQuiz = false;
      } else if (this.health == 1) {
        this.startQuiz = false;
        this.$emit("quizStartValue", this.startQuiz);
        this.quizEnd = true;
        this.$emit("quizEndValue", this.quizEnd);
      } else {
        this.currentQuestion += 1;
        this.health -= 1;
        this.countDown = 10;
        // this.progressWidth = 100;
        this.countDownTimer();
      }
    },
    questionsAmountFunc() {
      this.questionsAmount = this.questions.length;
    },
    nextQuestion() {
      this.incorrect = false;
      this.currentQuestion += 1;
      // this.progressWidth = 100;
      this.showAnswers = true;

      this.countDownTimer();
    },
    answerClick(isCorrect) {
      clearTimeout(this.timer);

      if (isCorrect) {
        // console.log(this.quizStore);
        this.quizStore.score += 3;
      }
      let nextQuestion = this.currentQuestion + 1;
      if (nextQuestion < this.questions.length) {
        this.currentQuestion = nextQuestion;
        // this.progressWidth = 100;
        this.countDown = 10;
        this.countDownTimer();
      }
      if (this.health == 1) {
        this.startQuiz = false;
        this.$emit("quizStartValue", this.startQuiz);
        this.quizEnd = true;
        this.$emit("quizEndValue", this.quizEnd);
      }

      if (!isCorrect) {
        this.showAnswers = false;
        // this.progressWidth = 0;
        clearTimeout(this.timer);
        this.currentQuestion -= 1;
        this.health -= 1;
        this.incorrect = true;
      } else if (nextQuestion == this.questions.length) {
        this.startQuiz = false;
        this.$emit("quizStartValue", this.startQuiz);
        this.quizEnd = true;
        this.$emit("quizEndValue", this.quizEnd);
      }
    },
  },
  mounted() {
    this.countDownTimer();
    this.questionsAmountFunc();
    Vue.axios.get("http://127.0.0.1:8000/api/questions/").then((response) => {
      console.log(response.data);
    });
  },
  created() {
    // console.log(this.countDown);
    // console.log(this.questionsAmount);
  },
  beforeUpdate() {
    // console.log(this.endGameBtn);
    if (this.endGameWarningBtn == true) {
      // alert("changed");
    }
  },
};
</script>
<style lang="scss" scoped>
#myBar {
  background: #ff9900;
}
.quiz {
  //   width: fit-content;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  max-width: 500px;
  width: 100%;
  @media only screen and (max-width: 420px) {
    max-width: 340px;
  }
  &__frame {
    margin-bottom: 7px;
    position: relative;
    .incorrect {
      position: absolute;
      width: 100%;
      height: 100%;
      // text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      background: rgba(0, 0, 0, 0.312);
      backdrop-filter: blur(5px);
      text-align: center;
      &__close {
        height: 20px;
        width: 20px;
        cursor: pointer;
        position: absolute;
        right: 20px;
        top: 15px;
      }
      &__title {
        font-size: 18px;
        padding: 0 70px;
        &-answertxt {
        }
      }
      &__nextQuestionBtn {
        text-decoration: none;
        color: #fff;
        background-color: #ff9900;
        padding: 4px 50px;
        cursor: pointer;
        position: absolute;
        bottom: 25px;

        font-size: 18px;
      }
    }
    .warning {
      position: absolute;
      width: 100%;
      height: 100%;
      // text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      background: rgba(0, 0, 0, 0.312);
      backdrop-filter: blur(5px);
      text-align: center;
      &__close {
        height: 20px;
        width: 20px;
        cursor: pointer;
        position: absolute;
        right: 20px;
        top: 15px;
      }
      &__title {
        // font-weight: 600;
        font-size: 18px;
        padding: 0 70px;
      }
      .endBtnLink {
        position: absolute;
        bottom: 25px;
        text-decoration: none;
      }
      &__endBtn {
        text-decoration: none;
        color: #fff;
        background-color: red;
        padding: 4px 50px;
        cursor: pointer;

        font-size: 18px;
      }
    }
    img {
      width: 500px;
      height: 300px;
      @media only screen and (max-width: 420px) {
        width: 340px;
        height: 210px;
      }
    }
  }
  &__info {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    .health {
      .heart {
        padding-right: 5px;
        @media only screen and (max-width: 420px) {
          height: 17px;
        }
      }
    }
    .numberOfQuestion {
      @media only screen and (max-width: 420px) {
        padding-right: 30px;
      }
    }
  }
  &__progress {
    padding-bottom: 10px;
    // background: #ff9900;
    // width: 80%;
    transition: width 1s linear;
  }
  .answersSection {
    @media only screen and (max-width: 420px) {
      width: 100%;
    }
    .showAnswers {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      @media only screen and (max-width: 420px) {
        justify-content: center;
      }
    }
    .answerBtn {
      font-size: 16px;
      background-color: #383838;
      border: 3px solid transparent;
      border-radius: 4px;
      width: 240px;
      color: #fff;
      padding-top: 13px;
      padding-bottom: 13px;
      cursor: pointer;
      margin-bottom: 10px;
      @media only screen and (max-width: 420px) {
        cursor: none;
        width: 100%;
        padding-top: 7px;
        padding-bottom: 7px;
      }

      &:hover {
        border: 3px solid #ff9900;
        @media only screen and (max-width: 420px) {
          border: none;
        }
      }
    }
  }
}
</style>
