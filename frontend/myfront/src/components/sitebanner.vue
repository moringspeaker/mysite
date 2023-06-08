<template>
  <div :style="{ backgroundImage: 'url(' + imageUrl + ')' }" class="banner">
      <div class="flex-column justify-content-center" style="position: relative" >
          <div id="title" class= "text-center mt-auto">
            <p class="site-title ">
              <a id="webtitle" href="App.vue">Chenyu Gu's website
              </a>
            </p>
            <p class="slogn">{{ slogn }}</p>
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
a{
  text-decoration: none;
}
.banner {
  /* Set the height of the banner */
  height: 250px;

  /* Set the width of the banner */
  width: 100%;

  /* Center and scale the background image */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  opacity: 0.8;
}
#title{
  position: relative;
  top: 70px;
}

.site-title {
  text-align: center;
  color: white;
  font-size: 20px;
  font-family: "Arial Black";

}

#webtitle{
  font-family: OribitronM;
  font-size: 50px;
  color:  white;
}

.slogn{
  font-family: Lobster;
  text-align: center;
  color: #88ffcc;
  font-size: 30px;
}
</style>