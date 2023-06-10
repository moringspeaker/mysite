<template>
  <div :style="{ backgroundImage: 'url(' + imageUrl + ')' }" class="banner">
      <div class="flex-column justify-content-center" style="position: relative" >
          <div id="title" class= "text-center mt-auto">
            <h1 class="site-title ">
              <a id="webtitle" href="App.vue">{{ Title }}
              </a>
            </h1>
            <h4 id="slogan" class="slogan">{{ slogan }}</h4>
          </div>
      </div>
  </div>
</template>

<script>

import BannerImage from '@/assets/BgImg/banner.jpg';
export default {
  name: "site-banner",
  props:{
    lang:{
      type:String,
      default:"EN"
    }
  },
  data(){
    return {
      Title:"Chenyu Gu's Website",
      slogan: "Live life. Learn lessons. Liberate yourself.",
      imageUrl: BannerImage,
    }
  },
  watch:{
    lang(newLang){
      if (newLang === "EN") {
        document.getElementById("webtitle").style.fontFamily="OribitronM";
        this.Title = "Chenyu's Website";
        this.slogan = "Live life. Learn lessons. Liberate yourself.";
      } else if (newLang === "中文") {
        document.getElementById("webtitle").style.fontFamily="MSZ";
        this.Title = "尘语的网站";
        this.slogan = "宇宙以其不息的欲望将一个歌舞炼为永恒，\n" +
            "这欲望有怎样一个人间的姓名，\n" +
            "大可忽略不计。";
      }
    }
  }
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
  top: 4.5rem;
}

.site-title {
  text-align: center;
  color: white;

  font-family: "Arial Black";

}

#webtitle{
  font-family: OribitronM;
  color:  white;
  font-size: 4rem;
}

#slogan{
  font-family: ZCOOL;
  text-align: center;
  color: #88ffcc;
  font-size: 1.5rem;
}
</style>