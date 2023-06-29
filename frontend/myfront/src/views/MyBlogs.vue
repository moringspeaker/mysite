<template>
  <div class="blogcontent-wrapper">
    <div class="img-wrapper" v-show="lang==='EN'" :style="getbgimg">
      <h2 class="position1">Now you are at:</h2>
      <h2 class="position2">/Blog Page</h2>
    </div>
    <div class="img-wrapper" v-show="lang!=='EN'" :style="getbgimg">
      <h2 class="position1">你的位置是:</h2>
      <h2 class="position2">/我的博客</h2>
    </div>
    <div class="content-wrapper">
      <blog-navbar :lang="lang"  />
      <div class="blog-container">
        <div v-html="welcome"/>
      </div>
    </div>

  </div>
  <blog-footer/>
</template>

<script>
import bgimg from '@/static/blog-background.png'
import source from '@/assets/markdown-sample.md'

import BlogNavbar from "@/components/BlogNavbar.vue";
import BlogFooter from "@/components/BlogFooter.vue";
import instance from "@/utils/request";
import md from "@/markdownParser";

export default {
  name: "MyBlogs",
  components: {
    BlogNavbar,
    BlogFooter,
  },
  props:['getlang'],
  data(){
    return{
      bgimg:bgimg,
      sentlang: '',
      blogdata: {},
      BlogId: '',
      welcome: '',
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
    lang() {
      return this.$store.state.lang;
    }
  },
  async mounted() {
    try {
      const response = await instance.get(`${process.env.VUE_APP_BACKEND_URL}blogs/api/blogs/`);
      this.blogdata = response.data;
      console.log(this.blogdata);
    } catch (error) {
      console.error(error);
    }
  },
  created() {
    this.welcome = md.render(source);
  },
}
</script>

<style scoped>
.blogcontent-wrapper{
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
.blog-container {
  background-color: #222222;
  color: #f0f0f0;
  width: 85%;
  padding: 15px;
  margin-top: 3vh;
  float: left;
  border: 2px solid #222222;
  border-radius: 10px;
}
</style>