<template>
  <div class="banner-wrapper">
    <div class="img-wrapper" v-show="lang==='EN'" :style="getbgimg">
      <h2 class="position1">Now you are at:</h2>
      <h2 class="position2">/Blog Page</h2>
    </div>
      <div class="img-wrapper" v-show="lang!=='EN'" :style="getbgimg">
        <h2 class="position1">你的位置是:</h2>
        <h2 class="position2">/我的博客</h2>
      </div>
    <div class="content-wrapper">
      <blog-category :lang="lang" :blogs="blogs"/>
    </div>
  </div>
</template>

<script>
import bgimg from '@/static/blog-background.png'

import BlogCategory from "@/components/BlogCategory.vue";
import instance from "@/utils/request";

export default {
  name: "MyBlogs",
  components: {
    BlogCategory,
  },
  props:['getlang'],
  data(){
    return{
      bgimg:bgimg,
      lang: 'EN',
      sentlang: '',
    }
  },
  watch:{
    getlang: function (data){
      this.lang = data;
      // this.sentlang = data;
    }
  },
  computed:{
    getbgimg(){
      return{
        backgroundImage: `url(${this.bgimg})`,
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
        backgroundPosition: 'center'
      }
    },
  },
  async mounted() {
    try {
      const response = await instance.get('http://localhost:8000/api/homepage/');
      this.homedata = response.data;
      this.swipers = this.homedata.swipers; // Make sure to use lowercase 'swipers'
      this.blogs = this.homedata.blogs;
      console.log("blog_view"+this.blogs)
    } catch (error) {
      console.error(error);
    }
  },
}
</script>

<style scoped>
.banner-wrapper{
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.img-wrapper{
  height: 25%;
  width: 100%;
  border-radius: 10px;
  justify-items: center;
  align-items: center;
}
.position1{
  margin-top: 15% ;
  color: #f0f0f0;
  text-align: center;
  font-family: FiraSan;
  font-size: 3rem;
}
.position2{

  color: wheat;
  text-align: center;
  font-family: FiraSan;
  font-size: 2.5rem;
}
.content-wrapper{
  height: 80%;
  width: 95%;
  justify-content: flex-start;
  display: grid;
  grid-template-columns: 75% 25%;
  grid-column-gap: 10px;
  grid-auto-rows: minmax(8rem, auto);
  grid-auto-flow: column dense;
}
</style>