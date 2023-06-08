<template>
  <div :style="{ backgroundImage: 'url(' + imageUrl + ')' }" class="banner">
    <div class="card-img-overlay">
      <div class="flex-lg-wrap">
        <div class="logo">
          <div class= "site-identity">
            <p class="site-title ">
              <a href="HelloWorld.vue">Chenyu Gu's website
              </a>
            </p>
            <p class="slogn">{{ slogn }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import BannerImage from '@/assets/BgImg/banner.jpg';
export default {
  name: "site-banner",
  data(){
    return {
      slogn: "Live life. Learn lessons. Liberate yourself.",
      imageUrl: BannerImage,
    }
  },
}
</script>

<style scoped>
.banner {
  /* Set the height of the banner */
  height: 200px;

  /* Set the width of the banner */
  width: 100%;

  /* Center and scale the background image */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  opacity: 0.7;
}
.site-title {
  text-align: center;
  color: white;
  font-size: 20px;
  font-family: "Arial Black";

}
.slogn{
  text-align: center;
  color: white;
  font-size: 20px;
}
</style>