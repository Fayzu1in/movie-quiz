<template>
  <div class="card">
    <div class="subscribe">
      <p class="subscribe__name">{{ name }}</p>
      <p class="subscribe__period">{{ period }}</p>
      <div class="subscribe__price">
        {{ price }}
        <img class="subscribe__price-icon" src="@/assets/img/star.png" alt="" />
      </div>
    </div>
    <button class="buyButton">Приобрести</button>
  </div>
</template>
<script>
export default {
  props: ["name", "period", "price"],
};
</script>
<style lang="scss" scoped>
.card {
  max-width: 364px;
  width: 100%;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  border: 4px solid transparent;

  &:hover {
    border: 4px solid #ff9900;
    border-radius: 4px;
    @media only screen and (max-width: 420px) {
      border: 4px solid transparent;
    }
  }

  @media only screen and (max-width: 420px) {
    max-width: 320px;
    // align-items: center;
    margin-bottom: 15px;
  }

  .subscribe {
    display: flex;
    flex-direction: column;
    background-image: url("@/assets/img/bckg.png");
    height: 160px;
    align-items: center;
    justify-content: space-around;
    background-color: rgba(0, 0, 0, 0.41);

    @media only screen and (max-width: 420px) {
      padding: 10px 0;
      height: 140px;
      justify-content: space-around;
    }

    &__name {
      font-size: 22px;
      // font-weight: 600;

      @media only screen and (max-width: 420px) {
        font-size: 18px;
        padding-top: 0px;
        font-weight: 600;
      }
    }
    &__period {
      font-size: 27px;
      margin: 0;
      // padding-bottom: 19px;
      @media only screen and (max-width: 420px) {
        font-size: 20px;
        padding-bottom: 0;
        // font-weight: 600;
      }
    }
    &__price {
      font-size: 27px;

      // padding-bottom: 22px;
      @media only screen and (max-width: 420px) {
        font-size: 22px;
        padding-bottom: 0px;
        // font-weight: 600;
      }
      img {
        height: 22px;
        @media only screen and (max-width: 420px) {
          height: 17px;
        }
      }
    }
  }
  .buyButton {
    // background: #ff9900;
    background: #383838;
    border: none;
    color: #fff;

    border-bottom-right-radius: 4px;
    border-bottom-left-radius: 4px;
    font-size: 18px;
    cursor: pointer;
    padding-top: 12px;
    padding-bottom: 12px;
    @media only screen and (max-width: 420px) {
      // font-size: 16px;
      padding-top: 7px;
      padding-bottom: 7px;
    }
  }
}
</style>
