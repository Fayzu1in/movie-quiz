<template>
  <div>
    <div class="quiz">
      <div class="quiz__info">
        <div class="health">
          <img src="@/assets/img/heart.png" class="heart" />
          <img src="@/assets/img/heart.png" class="heart" />
          <img src="@/assets/img/heart.png" class="heart" />
        </div>
        <div class="numberOfQuestion">{{ questionN }}/15</div>
        <div class="time">00:04</div>
      </div>
      <div class="quiz__progress"></div>
      <div class="quiz__frame">
        <img src="@/assets/img/frame.png" alt="" />
      </div>
      <div class="quiz__questions"></div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      heart: "heart.png",
      questionN: 1,
    };
  },
};
</script>
<style lang="scss">
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
    background: #ff9900;
    width: 80%;
  }
}
</style>
