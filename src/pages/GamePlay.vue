<template>
  <div>
    <div class="container gameSection">
      <div class="gamePlay">
        <div class="scoreInfo">
          <div class="scoreInfo__name">User Name</div>
          <div class="scoreInfo__score">
            0
            <img src="@/assets/img/star.png" alt="" />
          </div>
          <button class="scoreInfo__endGameBtn">Завершить</button>
        </div>
      </div>
    </div>
    <div class="quizCard container">
      <quiz-start></quiz-start>
    </div>
  </div>
</template>
<script>
import QuizStart from "../components/QuizStart.vue";
export default {
  components: {
    QuizStart,
  },
};
</script>
<style lang="scss">
.quizCard {
  display: flex;
  justify-content: center;
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
