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
          <!-- <img src="@/assets/img/heart.png" class="heart" />
          <img src="@/assets/img/heart.png" class="heart" /> -->
        </div>
        <div class="numberOfQuestion">{{ questionsAmount }}/15</div>
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
        <!-- <img src="@/assets/img/frame.png" alt="" /> -->
        <img :src="questions[0].questionImage" alt="" />
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
export default {
  components: {},
  // inject: ["countDown", "timer"],
  inject: ["score"],

  data() {
    return {
      currentQuestion: 0,
      progressWidth: 100,
      countDown: 10,
      timer: null,
      questionsAmount: 0,
      health: 3,
      questions: [
        {
          questionText: "Ты гей?",
          questionImage: "/hollywood.jpg",
          answerOptions: [
            { answerText: "Ты дебил", isCorrect: true },
            { answerText: "Не дебил", isCorrect: false },
            { answerText: "Дебилище", isCorrect: false },
            { answerText: "Этот вопрос сосет", isCorrect: false },
          ],
        },
        {
          questionText: "Ты пидор?",
          questoinImage: "",
          answerOptions: [
            { answerText: "Да я 100% пидор", isCorrect: true },
            { answerText: "Да я 10% пидор", isCorrect: false },
            { answerText: "Да я 50% пидор", isCorrect: false },
            { answerText: "Да я 90% пидор", isCorrect: false },
          ],
        },
        {
          questionText: "Ты черт?",
          questoinImage: "",
          answerOptions: [
            { answerText: "Да я 100% черт", isCorrect: true },
            { answerText: "Да я 10% черт", isCorrect: false },
            { answerText: "Да я 50% черт", isCorrect: false },
            { answerText: "Да я 90% черт", isCorrect: false },
          ],
        },
        {
          questionText: "Ты черт?",
          questoinImage: "",
          answerOptions: [
            { answerText: "Да я 100% черт", isCorrect: true },
            { answerText: "Да я 10% черт", isCorrect: false },
            { answerText: "Да я 50% черт", isCorrect: false },
            { answerText: "Да я 90% черт", isCorrect: false },
          ],
        },
      ],
    };
  },

  methods: {
    countDownTimer() {
      if (this.countDown > -1) {
        this.timer = setTimeout(() => {
          this.countDown -= 1;
          this.progressWidth -= 10;
          this.countDownTimer();
        }, 1000);
      } else {
        this.countDown = 10;
        this.progressWidth = 100;
      }
    },
    questionsAmountFunc() {
      // for (let i = 0; i < this.questions.length; i++) {
      //   console.log(i + 1);
      // }

      this.questionsAmount = this.questions.length;
    },
    answerClick(isCorrect) {
      clearTimeout(this.timer);
      let nextQuestion = this.currentQuestion + 1;
      if (isCorrect) {
        this.score = this.score + 1;
      }
      if (nextQuestion < this.questions.length) {
        this.currentQuestion = nextQuestion;
      }
    },
  },
  mounted() {
    this.countDownTimer();
    this.questionsAmountFunc();
  },
  created() {
    // console.log(this.countDown);
    console.log(this.questionsAmount);
  },
};
</script>
<style lang="scss" scoped>
#myBar {
  // width: 50%;
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
      max-width: 500px;
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
