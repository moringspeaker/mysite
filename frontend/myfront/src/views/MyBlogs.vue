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
      <blog-display :lang="lang"  />
    </div>

  </div>
  <blog-footer/>
</template>

<script>
import bgimg from '@/static/blog-background.png'

import BlogDisplay from "@/components/BlogDisplay.vue";
import BlogFooter from "@/components/BlogFooter.vue";
import instance from "@/utils/request";
export default {
  name: "MyBlogs",
  components: {
    BlogDisplay,
    BlogFooter,
  },
  props:['getlang'],
  data(){
    return{
      bgimg:bgimg,
      lang: 'EN',
      sentlang: '',
      blogdata: {},
      BlogId: '',
    }
  },
  watch:{
    getlang: function (data){
      this.lang = data;
    },
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
      const response = await instance.get('http://localhost:8000/blogs/api/blogs/');
      this.blogdata = response.data;
      console.log(this.blogdata);
    } catch (error) {
      console.error(error);
    }
  },
}
</script>

<style scoped>
.banner-wrapper{
  width: 100%;
  display: flex;
  flex-direction: column;
  overflow: auto;
}
.img-wrapper{
  height: 35vh;
  width: 100%;
  border-radius: 10px;
  justify-items: center;
  align-items: center;
}
.position1{
  margin-top: 15vh ;
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
  width: 99%;
  justify-content: flex-start;
  display: flex;
  flex-direction: row;
  justify-items: center;
  align-items: start;
}
</style>