<template>
  <div class="page-wrapper">
    <div class="img-wrapper" v-show="lang==='EN'" :style="getbgimg">
      <h2 class="position1">Now you are at:</h2>
      <h2 class="position2">/Blog Page</h2>
    </div>
    <div class="img-wrapper" v-show="lang!=='EN'" :style="getbgimg">
      <h2 class="position1">你的位置是:</h2>
      <h2 class="position2">/我的博客</h2>
    </div>
    <NavBar/>
        <div class="content-wrapper">
          <div class="inner-wrapper">
            <blog-navbar :lang="lang" class="blog-nav" />
            <div class="blog-container">
              <div v-html="markdownContent"/>
            </div>
            <markdown-toc :markdown="rawmarkdown" @clickItem="handleItemClick"
                          @headers-computed="headers = $event"
                          :scrollTo="scrollTo"
                          class="toc"
            >
            </markdown-toc>
          </div>
        </div>
  </div>
</template>

<script>
import bgimg from '@/static/blog-background.png'
import md from '@/markdownParser';
import instance from "@/utils/request";
import BlogNavbar from "@/components/BlogNavbar.vue";
import MarkdownToc from "@/components/markdownTOC.vue";
import NavBar from "@/components/NavBar.vue";
export default {
  name: "MyBlogs",
  components: {
    BlogNavbar,
    MarkdownToc,
    NavBar,

  },
  props:['getlang','id'],
  data(){
    return{
      bgimg:bgimg,
      blogid: '',
      blogcontent: '',
      markdownContent: '',
      rawmarkdown: '',
      currentHeaderIndex: '',
      tocx: '',
      tocy:'',
      hei:null,
    }
  },
  setup(){
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
    },
  },
  methods:{
    scrollToAnchor(id) {
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({
          behavior: 'smooth',
          block: 'start',
        });
      }
    },
    handleItemClick(e) {
      this.currentHeaderIndex = e.index;
      console.log("id========");
      console.log(e.item.id);
      this.scrollToAnchor(e.item.id);
    },
  },

  async mounted() {

    try {
      const blogId = this.$route.params.id;
      let backendUrl = process.env.VUE_APP_BACKEND_URL;
      console.log()
      const response = await instance.get(`${backendUrl}blogs/api/blogs/${blogId}`);
      this.blogcontent = response.data;

      if (this.lang==='EN'){
        const blogmd = this.blogcontent.ENcontent;
        this.markdownContent = md.render(blogmd);
        this.rawmarkdown = blogmd;
      }
      else {
        const blogmd = this.blogcontent.CHcontent;
        this.rawmarkdown = blogmd;
        this.markdownContent = md.render(blogmd);
      }
    } catch (error) {
      console.error(error);
    }
  },

}
</script>

<style scoped>
.page-wrapper{
  width: 100%;
  display: flex;
  flex-direction: column;
  overflow: scroll;
}
.img-wrapper{
  height: 20vh;
  width: 100%;
  border-radius: 10px;
  justify-items: center;
  align-items: center;
}
.position1{
  margin-top: 5vh ;
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
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-items: start;
}
.inner-wrapper{
  width: 100rem;
  display: grid;
  grid-template-columns: 15% 65% 20%;
  grid-gap: 10px;
  background-color: #2E4F4F;
  grid-template-rows: 1fr 1fr 1fr;
}
.blog-nav{
  grid-column: 1/2;
  width: 15rem;
}
.blog-container {
  height: 100%;
  background-color: #222222;
  color: #f0f0f0;
  grid-column: 2/3;
  grid-row: 1/4;
  padding: 15px;
  margin-top: 3vh;
  margin-left: 10px;
  float: left;
  border: 2px solid #222222;
  border-radius: 10px;
  overflow: scroll;
}
.toc{
  grid-column: 3/4;
  position: sticky;
  top:10px;
}
</style>