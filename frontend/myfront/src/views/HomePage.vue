<template>
  <div class="inner-wrapper">
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
        <div class="subtitle" v-show="currentLanguage.value==='EN'">
          {{ img.ENtitle }}
        </div>
        <div class="subtitle" v-show="currentLanguage.value!=='EN'">
          {{ img.CHtitle }}
        </div>
      </swiper-slide>
    </swiper>
      <div class="components-container">
        <blog-window :lang="currentLanguage.value" :blogs="blogs" class="content-wrapper"/>
        <about-me :lang="currentLanguage.value" class="aboutme"/>
      </div>
      <!--    <AudioPlayer/>-->
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

import { mapGetters } from 'vuex';
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

import NoImg from "@/static/no-image.png"


import { formatDatetime } from '@/utils/datetimeUtils';

export default {
  components: {
    BlogWindow,
    Swiper,
    SwiperSlide,
    AboutMe,
    // AudioPlayer,
  },
  props:['getlang'],  // the same method declared in parent component, which is App.vue in this project
  methods: {
    getImageUrl(imageSrc) {
      // Modify the image source URL here
      console.log(`${process.env.VUE_APP_BACKEND_URL}${imageSrc}`);
      return `${process.env.VUE_APP_BACKEND_URL}${imageSrc}`;
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
  computed: {
    ...mapGetters([
      'currentLanguage',  // add this line
    ])
  },

  async mounted() {
    const response = await instance.get(`${process.env.VUE_APP_BACKEND_URL}api/homepage/`);
    console.log('000000000');
    console.log(response);
    try {
      const response = await instance.get(`${process.env.VUE_APP_BACKEND_URL}api/homepage/`);
      this.homedata = response.data;
      this.swipers = this.homedata.swipers; // Make sure to use lowercase 'swipers'
      this.blogs = this.homedata.blogs;
      this.blogs.forEach(blog => {
        blog.created_date = formatDatetime(blog.created_date,"YYYY-MM-DD");
      });
      console.log(this.swipers);
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
      modules: [Navigation, Pagination, Scrollbar, A11y, Autoplay],
    };
  },
};
</script>

<style>
.inner-wrapper{
  height: 100vh;
  width: 100%;
  display: grid;
  grid-template-rows: 30% 70%;
  grid-row-gap: 10px;
  grid-template-columns: 74% 24.5% 1.5%;
  grid-column-gap: 10px;
  padding: 20px;
}
.my-swiper {
  grid-row: 1/2;
  grid-column: 1/3;
  width: 60%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #2E4F4F;

  /* Center slide text vertically */
  display: flex;
  align-items: center;
  flex-direction: column;
  border-radius: 10px;
}

.swiper-slide img {
  display: flex;
  width: 100%;
  height: 85%;
  object-fit: cover;
  border-radius: 10px;
}
.subtitle {
  /* Styles for the subtitle */
  font-size: 25px;
  color: white;
  font-family: FiraSan;
}
.components-container{
  grid-column: 1/3;
  display: grid;
  grid-template-columns: 75% 25%;
  grid-column-gap: 10px;
  justify-content: flex-start;
}
.content-wrapper{
  height:60%;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.aboutme{
  height:50%;
  margin-top: 4rem;
}
</style>

