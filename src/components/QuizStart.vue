<template>
  <div>
    <div class="quiz">
      <div class="quiz__info">
        <div class="health">
          <img src="@/assets/img/heart.png" class="heart" />
          <img src="@/assets/img/heart.png" class="heart" />
          <img src="@/assets/img/heart.png" class="heart" />
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
        <img src="@/assets/img/frame.png" alt="" />
      </div>
      <div class="quiz__questions"></div>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  // inject: ["countDown", "timer"],
  data() {
    return {
      progressWidth: 100,
      countDown: 10,
      timer: null,
      questionsAmount: 0,
      questions: [
        {
          questionText: "Ты гей?",
          questoinImage: "",
          answerOptions: [
            { answerText: "Да я 100% гей", isCorrect: true },
            { answerText: "Да я 10% гей", isCorrect: false },
            { answerText: "Да я 50% гей", isCorrect: false },
            { answerText: "Да я 90% гей", isCorrect: false },
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
  },
  beforeMount() {
    this.countDownTimer();
    this.questionsAmountFunc();
  },
  created() {
    // console.log(this.countDown);
    console.log(this.questionsAmount);
  },
};
</script>
<style lang="scss">
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
  &__info {
    display: flex;
    justify-content: space-between;
    width: 100%;
  }
  &__progress {
    padding-bottom: 10px;
    // background: #ff9900;
    // width: 80%;
    transition: all 1s;
  }
}
</style>
