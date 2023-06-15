<template>
  <swiper
      class="my-swiper"
      :modules="modules"
      :slides-per-view="1"
      :space-between="0"
      :loop=true
      navigation
      :pagination="{ clickable: true }"
      :scrollbar="{ draggable: true }"
      @swiper="onSwiper"
      @slideChange="onSlideChange"
  >
    <swiper-slide class="swiper-slide" v-for="(img, index) in imgUrl" :key="index">
      <img :src="img.src">
      <div class="subtitle" v-show="lang==='EN'">
        {{ img.EN }}
      </div>
      <div class="subtitle" v-show="lang!=='EN'">
        {{ img.CH }}
      </div>
    </swiper-slide>
  </swiper>
  <div class="content-wrapper">
    <blog-window :sentlang="sentlang"/>
  </div>

</template>


<script>
// import Swiper core and required modules
import { Navigation, Pagination, Scrollbar, A11y } from 'swiper';
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/autoplay'
// Import Swiper styles

import BlogWindow from "@/views/BlogWindow.vue";

export default {
  components: {
    BlogWindow,
    Swiper,
    SwiperSlide,
  },
  props:['getlang'],  // the same method declared in parent component, which is App.vue in this project
  data(){
    return{
      imgUrl: [],
      images:[
        {src:'https://i.imgur.com/SlX7B65.png',EN: 'hi', CH: '你好'},
        {src:'https://i.imgur.com/k0ItOuT.png',EN: 'hi', CH: '你好'},
        {src:'https://i.imgur.com/Tj5VR88.png',EN: 'hi', CH: '你好'},
      ],
      lang: 'EN',
      sentlang:'',
    }
  },
  watch:{
    getlang: function (data){
      this.lang = data;
      this.sentlang = data;
      // console.log(this.lang)
    }
  },
  methods:{
    async fetchImage() {
      for (let i in this.images) {
        fetch(this.images[i].src) // Use this.images[i].src instead of i.src
            .then((response) => response.blob())
            .then((blob) => {
              console.log(blob);
              this.imgUrl.push({
                src: URL.createObjectURL(blob),
                EN: this.images[i].EN, // Use this.images[i].EN instead of i.EN
                CH: this.images[i].CH, // Use this.images[i].CH instead of i.CH
              });
              console.log(this.imgUrl);
            })
            .catch((error) => {
              console.error('Error fetching image:', error);
            });
      }
    },
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
      modules: [Navigation, Pagination, Scrollbar, A11y],
    };
  },
  beforeMount() {
    this.fetchImage();
  }
};
</script>

<style>
.my-swiper {
  width: 60%;
  height: 20%;
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
  height: 100%;
  width: 100%;
  justify-content: flex-start;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}
</style>

