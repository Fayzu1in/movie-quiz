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
  background-image: url("@/assets/img/bckg.png");
  max-width: 370px;
  width: 100%;
  display: flex;
  flex-direction: column;
  .subscribe {
    display: flex;
    flex-direction: column;
    align-items: center;
    &__name {
      font-size: 22px;
    }
    &__period {
      font-size: 32px;
      margin: 0;
      padding-bottom: 19px;
    }
    &__price {
      font-size: 32px;
      padding-bottom: 22px;
    }
  }
  .buyButton {
    background: #ff9900;
    color: #fff;
    border: none;
    font-size: 18px;
    cursor: pointer;
    padding-top: 12px;
    padding-bottom: 12px;
  }
}
</style>
