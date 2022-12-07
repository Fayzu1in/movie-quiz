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
        :style="{
          width: progressWidth + '%',
        }"
      ></div>

      <div class="quiz__frame">
        <img :src="questions[currentQuestion].questionImage" alt="" />
      </div>
      <div class="answersSection">
        <button
          :key="index"
          v-for="(option, index) in questions[currentQuestion].answerOptions"
          class="answerBtn"
          @click="answerClick(option.isCorrect)"
        >
          {{ option.answerText }}
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import { useQuizStore } from "../store";
import { mapStores } from "pinia";
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

  data() {
    return {
      // startQuiz: false,
      currentQuestion: 0,
      progressWidth: 100,
      countDown: 10,
      timer: null,
      questionsAmount: 0,
      health: 3,
      startQuiz: true,
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
  },

  methods: {
    countDownTimer() {
      if (this.countDown > -1) {
        this.timer = setTimeout(() => {
          this.countDown -= 1;
          this.progressWidth -= 10;
          this.countDownTimer();
        }, 1000);
      } else if (this.questions.length - 1 == this.currentQuestion) {
        this.startQuiz = false;
        this.$emit("quizStartValue", this.startQuiz);
      } else if (this.health === 0) {
        this.startQuiz = false;
      } else {
        this.currentQuestion += 1;
        this.health -= 1;
        this.countDown = 10;
        this.progressWidth = 100;
        this.countDownTimer();
      }
    },
    questionsAmountFunc() {
      this.questionsAmount = this.questions.length;
    },

    answerClick(isCorrect) {
      clearTimeout(this.timer);
      let nextQuestion = this.currentQuestion + 1;
      if (isCorrect) {
        console.log(this.quizStore);
        this.quizStore.score += 3;
      }
      if (nextQuestion < this.questions.length) {
        this.currentQuestion = nextQuestion;
        this.progressWidth = 100;
        this.countDown = 10;
        this.countDownTimer();
      }
      if (this.health == 1) {
        this.startQuiz = false;
        this.$emit("quizStartValue", this.startQuiz);
      }
      if (!isCorrect) {
        this.health -= 1;
      } else if (nextQuestion == this.questions.length) {
        this.startQuiz = false;
        this.$emit("quizStartValue", this.startQuiz);
      }
    },
  },
  mounted() {
    this.countDownTimer();
    this.questionsAmountFunc();
  },
  created() {
    // console.log(this.countDown);
    // console.log(this.questionsAmount);
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
  &__frame {
    margin-bottom: 7px;
    img {
      width: 500px;
      height: 300px;
    }
  }
  &__info {
    display: flex;
    justify-content: space-between;
    width: 100%;
    .health {
      .heart {
        padding-right: 5px;
      }
    }
  }
  &__progress {
    padding-bottom: 10px;
    // background: #ff9900;
    // width: 80%;
    transition: all 1s linear;
  }
  .answersSection {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;

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

      &:hover {
        border: 3px solid #ff9900;
      }
    }
  }
}
</style>
