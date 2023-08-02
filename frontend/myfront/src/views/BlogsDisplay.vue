<template>
  <div class="page-wrapper">
    <div class="img-wrapper" v-show="lang==='EN'" :style="getbgimg">
      <transition >
        <h2 class="position1" v-if="pageLoaded">Now you are at:</h2>
      </transition>
      <transition >
        <h2 class="position2" v-if="pageLoaded">/Blog Page: Results of {{  }}</h2>
      </transition>
    </div>

    <div class="img-wrapper" v-show="lang!=='EN'" :style="getbgimg">
      <transition >
      <h2 class="position1" v-if="pageLoaded">你的位置是:</h2>
      </transition>
      <transition >
      <h2 class="position2" v-if="pageLoaded">/我的博客:{{  }}</h2>
      </transition >
    </div>
    <NavBar class="navbar"/>
    <div class="content-container">
        <div class="inner-container">
        <div class="left-side-bar">
            <recent-blogs  class="re-blogs" />
            <collect-category class="co-blogs"/>
        </div>
        <div class="right-side">
            <blog-window :lang="lang" :blogs="search_blogs" class="blogg-window"/>
        </div>
        </div> 
    </div>
    <el-pagination 
        :background="true" 
        layout="prev, pager, next" 
        :total="pageNum" 
        :page-count="pageNum"
        class="paginator"
        @current-change="handleCurrentChange">
    </el-pagination>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import bgimg from '@/static/blog-background.png'
import RecentBlogs from "@/components/RecentBlogs.vue";
import CollectCategory from "@/components/CollectCategory.vue";
import BlogWindow from '@/components/BlogWindow.vue';
import instance from "@/utils/request";


export default {
  name: "BlogsDisplay",
  components:{
    NavBar,
    RecentBlogs,
    CollectCategory,
    BlogWindow,
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
    search(){
        return this.$store.state.search;
    }
  },
   data(){
    return{
      bgimg:bgimg,
      hei: null,
      pageLoaded: true,
      search_blogs: "",
      questionsList: [],
      pageNum: 0,
      currentPage: 1,
    }   
  },
   methods: {
    async handleCurrentChange(val) {
        this.currentPage = val;
        try {
            const response = await instance.post(`${process.env.VUE_APP_BACKEND_URL}api/blogs/`, { page: val });
            if (response && response.data) {
            this.search_blogs = response.data.results; 
            let counts = response.data.count;
            this.pageNum =  Math.ceil(counts / 6);
            }
        } catch (error) {
            console.error(error);
        }
    },
  },
  async mounted() {
    try{
        const response = await instance.post(`${process.env.VUE_APP_BACKEND_URL}api/blogs/`, { page: 1 });
        if (response && response.data) {
        this.search_blogs = response.data.results;
        let counts = response.data.count;
        this.pageNum =  Math.ceil(counts / 6);
        }
    }
     catch (error) {
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
  align-items: center;
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
.navbar{
    width: 100%;
}
.content-container{
  width: 100%;
  display: flex;
  flex-direction: row;

}

.inner-container{
  width: 100%;
  display: flex;
  flex-direction: row;
  background: transparent;

}
.left-side-bar{
  width: 20%;
  margin-top: 0;
  display: flex;
  flex-direction: column;
}
.right-side{
  width: 80%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}
.blogg-window{
    height: 100%;
    width: 100%;
}
.el-pagination .el-pager li.active.number {
    background-color: #333333;
}
.paginator{
  align-self: center;  /* This will center the paginator if the parent is a flex container */
  margin: 10px 0; 
}
</style>