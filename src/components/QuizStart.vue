<template>
  <div>
    <div class="quiz">
      <div class="quiz__info">
        <div class="health">
          <img src="@/assets/img/heart.png" class="heart" />
          <img src="@/assets/img/heart.png" class="heart" />
          <img src="@/assets/img/heart.png" class="heart" />
        </div>
        <div class="numberOfQuestion">{{}}/15</div>
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
  inject: ["countDown", "timer"],
  data() {
    return {
      progressWidth: 100,
    };
  },

  methods: {},
  created() {
    console.log(this.countDown);
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
