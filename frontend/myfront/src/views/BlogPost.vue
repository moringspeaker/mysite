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
      <blog-navbar :lang="lang"  />
      <div class="blog-container">
        <div v-html="markdownContent"/>
      </div>
      <markdown-toc :markdown="rawmarkdown" @clickItem="handleItemClick"
                    @headers-computed="headers = $event"
                    :scrollTo="scrollTo"
                    :style="{ postion:'fixed', top: tocx + 'px', left: tocy + 'px' }"
      >
      </markdown-toc>
    </div>

  </div>
  <blog-footer/>
</template>

<script>
import bgimg from '@/static/blog-background.png'
import md from '@/markdownParser';
import BlogFooter from "@/components/BlogFooter.vue";
import instance from "@/utils/request";
import BlogNavbar from "@/components/BlogNavbar.vue";
import MarkdownToc from "@/components/markdownTOC.vue";
export default {
  name: "MyBlogs",
  components: {
    BlogNavbar,
    BlogFooter,
    MarkdownToc,
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
    getblog(blogUrl) {
  // Modify the image source URL here
      return `${process.env.VUE_APP_BACKEND_URL}${blogUrl}`;
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
        let blogmdUrl = this.getblog(this.blogcontent.ENcontent);
        console.log(blogmdUrl);
        const blogmd  = await instance.get(blogmdUrl);
        this.rawmarkdown = blogmd.data;
        this.markdownContent = md.render(blogmd.data);
      }
      else {
        this.markdownContent = md.render(this.blogcontent.CHcontent);
      }
    } catch (error) {
      console.error(error);
    }
    //get the blog-container's position
    const blogContainer = document.querySelector('.blog-container');
    const blogContainerRect = blogContainer.getBoundingClientRect();
    const contentWrapper = document.querySelector('.content-wrapper');
    const contentWrapperRect = contentWrapper.getBoundingClientRect();

    this.tocx = blogContainerRect.top - contentWrapperRect.top
    this.tocy = blogContainerRect.right + 20;

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
.blog-container {
  background-color: #222222;
  color: #f0f0f0;
  width: 65%;
  padding: 15px;
  margin-top: 3vh;
  float: left;
  border: 2px solid #222222;
  border-radius: 10px;
}
</style>