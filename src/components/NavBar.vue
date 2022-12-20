<template>
  <div>
    <nav class="navbar container">
      <a class="navbar__left" href="https://allplay.uz/"
        ><img src="@/assets/img/allplay-logo.svg" alt=""
      /></a>

      <a class="navbar__right" href="">
        <img class="profileImg" src="@/assets/img/profile.jpg" alt="" />
      </a>
    </nav>
  </div>
</template>
<script>
export default {};
</script>
<style lang="scss" scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  padding-top: 14px;
  padding-bottom: 14px;
  margin-bottom: 14px;
  @media only screen and (max-width: 420px) {
    margin-bottom: 0px;
  }
  // 40px of bottom
}
.profileImg {
  height: 48px;
  border-radius: 50%;
}
</style>
