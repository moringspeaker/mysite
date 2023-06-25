<template>
  <swiper
      class="my-swiper"
      :modules="modules"
      :slides-per-view="1"
      :space-between="0"
      :autoplay="{
      delay: 2500,
      disableOnInteraction: false,
    }"
      :loop=true
      navigation
      :pagination="{ clickable: true }"
      :scrollbar="{ draggable: true }"
      @swiper="onSwiper"
      @slideChange="onSlideChange"
      @autoplayTimeLeft="onAutoplayTimeLeft"
  >
    <swiper-slide class="swiper-slide" v-for="(img, index) in swipers" :key="index">
      <img :src="getImageUrl(img.src)" :alt="noimg">
      <div class="subtitle" v-show="lang==='EN'">
        {{ img.ENtitle }}
      </div>
      <div class="subtitle" v-show="lang!=='EN'">
        {{ img.CHtitle }}
      </div>
    </swiper-slide>
  </swiper>
  <div class="content-wrapper">
    <blog-window :lang="lang" :blogs="blogs"/>
    <about-me :lang="lang" />
    <AudioPlayer/>
  </div>

</template>


<script>
// import my axios instance
import instance from '@/utils/request';
// import { ref } from 'vue';
// import Swiper core and required modules
import { Navigation, Pagination, Scrollbar, A11y, Autoplay, } from 'swiper';
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/autoplay'
// Import Swiper styles

//import other components
import BlogWindow from "@/components/BlogWindow.vue";
import AboutMe from "@/components/AboutMe.vue";
import AudioPlayer from "@/components/AudioPlayer.vue";

import NoImg from "@/static/no-image.png"
// import swipe from "bootstrap/js/src/util/swipe";

import { formatDatetime } from '@/utils/datetimeUtils';

export default {
  components: {
    BlogWindow,
    Swiper,
    SwiperSlide,
    AboutMe,
    AudioPlayer,
  },
  props:['getlang'],  // the same method declared in parent component, which is App.vue in this project
  methods: {
    getImageUrl(imageSrc) {
      // Modify the image source URL here
      console.log(`http://127.0.0.1:8000${imageSrc}`);
      return `http://127.0.0.1:8000${imageSrc}`;
    },
  },
  data(){
    return{
      noimg: NoImg,
      homedata: [],
      swipers: [],
      lang: 'EN',
      sentlang: '',
      blogs:[],
    }
  },
  watch:{
    getlang: function (data){
      this.lang = data;
      // this.sentlang = data;
    },

  },

  async mounted() {
    try {
      const response = await instance.get('http://localhost:8000/api/homepage/');
      this.homedata = response.data;
      this.swipers = this.homedata.swipers; // Make sure to use lowercase 'swipers'
      this.blogs = this.homedata.blogs;
      this.blogs.forEach(blog => {
        blog.created_date = formatDatetime(blog.created_date,"YYYY-MM-DD");
        console.log(blog.created_date);
      });

    } catch (error) {
      console.error(error);
    }
  },

  setup() {
    const onSwiper = (swiper) => {
      console.log(swiper);
    };
    const onSlideChange = () => {
      console.log('slide change');
    };
    return {
      onSwiper,
      onSlideChange,
      // onAutoplayTimeLeft,
      // progressCircle,
      // progressContent,
      modules: [Navigation, Pagination, Scrollbar, A11y, Autoplay],
    };
  },
};
</script>

<style>
.my-swiper {
  width: 60%;
  height:40vh;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #2E4F4F;

  /* Center slide text vertically */
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  align-items: center;
  flex-direction: column;
}

.swiper-slide img {
  display: flex;
  width: 100%;
  height: 85%;
  object-fit: cover;

}
.subtitle {
  /* Styles for the subtitle */
  font-size: 25px;
  color: white;
  font-family: FiraSan;

}

.content-wrapper{
  height: 140vh;
  width: 95%;
  justify-content: flex-start;
  display: grid;
  grid-template-columns: 75% 25%;
  grid-column-gap: 10px;
  grid-auto-rows: minmax(8rem, auto);
  grid-auto-flow: column dense;
}
</style>

