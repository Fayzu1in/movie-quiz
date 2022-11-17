<template>
  <div>
    <div class="card">
      <div class="subscribe">
        <p class="subscribe__name">{{ name }}</p>
        <p class="subscribe__period"></p>
        <div class="subscribe__price">
          <img class="subscribe__price-icon" src="" alt="" />
        </div>
      </div>
      <div class="buyButton"></div>
    </div>
  </div>
</template>
<script>
export default {
  data: function () {
    return {
      name: "Otsosi",
    };
  },
};
</script>
<style lang="scss" scoped>
.card {
  background-image: url("@/assets/img/bckg.png");
}
</style>
