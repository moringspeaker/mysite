<template>
  <div :style="{
      backgroundImage: 'url(' + imageUrl + ')',
      backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center center'
    }" 
   class="banner">
      <div class="flex-column justify-content-center" style="position: relative" >
          <div id="title" class= "text-center mt-auto">
            <h1 class="site-title ">
              <transition>
                <a id="webtitle" href="App.vue" v-if="pageloaded">{{ Title }}</a>
              </transition>
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
  data(){
    return {
      Title:"Chenyu Gu's Website",
      slogan: "Live life. Learn lessons. Liberate yourself.",
      imageUrl: BannerImage,
      pageloaded:false,
    }
  },
  computed:{
    lang(){
      return this.$store.state.lang;
    }
  },
  watch:{
    lang(newLang){
      console.log('111111111'+newLang);
      if (newLang === "EN") {
        document.getElementById("webtitle").style.fontFamily="OribitronM";
        this.Title = "Chenyu's Website";
        this.slogan = "Live life. Learn lessons. Liberate yourself.";
      } else if (newLang !== "EN") {
        document.getElementById("webtitle").style.fontFamily="WY";
        this.Title = "尘语的网站";
        this.slogan = "宇宙以其不息的欲望将一个歌舞炼为永恒，\n" +
            "这欲望有怎样一个人间的姓名，\n" +
            "大可忽略不计。";
      }
    }
  },
  mounted() {
    this.pageloaded = true;
  }
}
</script>

<style scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 1.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}


a{
  text-decoration: none;
}

.banner {
  /* Set the height of the banner */
  height: 25vh;
  /* Set the width of the banner */
  width: 100%;

  /* Center and scale the background image */
 background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  overflow: hidden;
  box-sizing: border-box;
}

.banner:before {
  content: "";
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0; /* This ensures the mask's height matches the banner's height */
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
  pointer-events: none;
}

#title{
  position: relative;
  top: 8vh;
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
  font-family: WuHun;
  text-align: center;
  color: #88ffcc;
  font-size: 1.5rem;
}
</style>