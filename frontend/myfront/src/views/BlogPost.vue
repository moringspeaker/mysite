<template>
  <div class="page-wrapper">

    <div class="img-wrapper" v-show="lang==='EN'" :style="getbgimg">
      <transition >
        <h2 class="position1" v-if="pageLoaded">Now you are at:</h2>
      </transition>
      <transition >
      <h2 class="position2" v-if="pageLoaded">/Blog Page: {{blogcontent.ENtitle}}</h2>
      </transition>
    </div>

    <div class="img-wrapper" v-show="lang!=='EN'" :style="getbgimg">
      <transition >
      <h2 class="position1" v-if="pageLoaded">你的位置是:</h2>
      </transition>
      <transition >
      <h2 class="position2" v-if="pageLoaded">/我的博客: {{blogcontent.CHtitle}}</h2>
      </transition >
    </div>

    <NavBar/>
        <div class="content-wrapper">
          <div class="inner-wrapper">
            <div class="left-side-bar">
              <recent-blogs  class="re-blogs" />
              <collect-category class="co-blogs"/>
            </div>
            <div class="blog-container" id="blog-render">
              <div v-html="markdownContent" ref="blogContainer"/>
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
import { onMounted, ref, watch } from 'vue'
import { useStore } from 'vuex'
import bgimg from '@/static/blog-background.png'
import md from '@/markdownParser';
import instance from "@/utils/request";
import MarkdownToc from "@/components/markdownTOC.vue";
import NavBar from "@/components/NavBar.vue";
import RecentBlogs from "@/components/RecentBlogs.vue";
import CollectCategory from "@/components/CollectCategory.vue";
export default {
  name: "MyBlogs",
  components: {
    RecentBlogs,
    CollectCategory,
    MarkdownToc,
    NavBar,
  },
  props:['getlang','id'],
  setup() {
    const store = useStore()
    const blogContainer = ref("blogContainer")
    const currentHeader = ref('') // add this to your data

    // Function to handle scroll event
    const handleScroll = () => {  //monitor user's scrolling
      let headers = blogContainer.value.querySelectorAll('h1, h2, h3, h4, h5, h6');
      let currentHeaderId = '';
      console.log("headers="+headers);
      for (let i = 0; i < headers.length; i++) {
        let bounding = headers[i].getBoundingClientRect();

        if (bounding.top > 0 && bounding.top < window.innerHeight) {
          currentHeaderId = headers[i].id;
          break;
        }
      }
      currentHeader.value = currentHeaderId;
      console.log('Current Header ID:', currentHeaderId); // log the current header ID
    }

    // add scroll event listener on component mounted
    onMounted(() => {
      var blogContainer = document.getElementById("blog-render");
      blogContainer.addEventListener('scroll', handleScroll);     //add an EventListener to your blog container
    })

    watch(currentHeader, (newVal) => {
      store.commit('setCurrentHeaderIndex', newVal)
    })

    return {
      blogContainer,
      currentHeader
    }
  },
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
      hei: null,
      pageLoaded: false,
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
    handleItemClick(e) {
      this.currentHeaderIndex = e.index;
      this.scrollToAnchor(e.item.id);
    },
  },
  watch:{
    lang(newLang){
      if (newLang==='EN'){
        const blogmd = this.blogcontent.ENcontent;
        this.markdownContent = md.render(blogmd);
        this.rawmarkdown = blogmd;
      }
      else {
        const blogmd = this.blogcontent.CHcontent;
        this.rawmarkdown = blogmd;
        this.markdownContent = md.render(blogmd);
      }
    }
  },
  async mounted() {
    this.pageLoaded = true;
    try {
      const blogId = this.$route.params.id;
      let backendUrl = process.env.VUE_APP_BACKEND_URL;
      const response = await instance.get(`${backendUrl}api/blogs/${blogId}`);
      this.blogcontent = response.data;
      console.log(this.blogcontent)
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

a{
  text-decoration: none;
  color: #fff3cd;
}
pre{
  border-radius: 10px;
}

.page-wrapper{
  width: 100%;
  display: flex;
  flex-direction: column;
  overflow: scroll;
  background-image: url("@/static/bg.gif");
  background-repeat: no-repeat;
  background-size: cover ;
  background-attachment: fixed;
}
.v-enter-active,
.v-leave-active {
  transition: opacity 1.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
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
  grid-template-columns: 20% 65% 15%;
  grid-gap: 10px;
  grid-template-rows: 1fr 1fr 1fr;
  background: transparent;
}
.left-side-bar{
  grid-column: 1/2;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
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