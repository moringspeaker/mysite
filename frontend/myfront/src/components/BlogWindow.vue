<template>
  <div class="latest-release ">
    <h2 v-show="lang==='EN'">Latest Release</h2>
    <h2 v-show="lang!=='EN'">最新发布</h2>
    <div class="blog-container">
      <div class="blog-item" v-for="(blog, index) in blogs" :key="index" @click="goToBlogPage(blog.id)">
        <div class="blog-box" :style="getBackgroundStyle(blog,index)">
         <div class=" img-wrapper" >
           <img class="blog-image" :src="getImageUrl(blog.cover)" :alt="placeholder">
         </div>
          <div class="blog-content" v-show="lang==='EN'">
            <h4>{{ blog.ENtitle }}</h4>
            <p class="summary">{{ blog.ENsummary }}</p>
            <p class="created-date block-display" id="timestamp">{{ blog.created_date }}</p>
          </div>
          <div class="blog-content" v-show="lang!=='EN'">
            <h4>{{ blog.CHtitle }}</h4>
            <p class="summary">{{ blog.CHsummary }}</p>
            <p class="created-date block-display" id="timestamp">{{ blog.created_date }}</p>
          </div> 
           <div class="blog-meta" v-show="lang==='EN'">
             <p class="authorname"> Created by:<span class="badge bg-secondary authortag">{{ blog.ENauthor }}</span></p>
             <p class="tags">tags:<span class="badge bg-secondary category"> {{ blog.category_name }}</span></p>
            <button class="btn btn-outline-light jump-button btn-sm" @click="goToBlogPage(blog.id)">Read...</button>
          </div>
          <div class="blog-meta" v-show="lang!=='EN'">
            <p class="authorname"> Created by:<span class="badge bg-secondary authortag" >{{ blog.CHauthor }}</span></p>
              <p class="tags">tags:<span class="badge bg-secondary category"> {{ blog.category_name }}</span></p>
            <button class="btn btn-outline-light jump-button btn-sm" @click="goToBlogPage(blog.id)">打开...</button>
          </div> 
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router'

import placeholder from '@/static/placeholder.png';

import bg1 from '@/static/blog-box/1.png';
import bg2 from '@/static/blog-box/2.png';
import bg3 from '@/static/blog-box/3.png';
import bg4 from '@/static/blog-box/4.png';
import bg5 from '@/static/blog-box/5.png';
import bg6 from '@/static/blog-box/6.png';
export default {
  name: "BlogWindow",

  props: {
    blogs: {
      type: Array, // Update the type to Array
      default: function () {
        return []; // Set the default value to an empty array
      },
    },
  },
  setup() {
    const router = useRouter();

    const goToBlogPage = (id) => {
      router.push(`/blogs/${id}`);
    };
    return {
      goToBlogPage,
    };
  },
  data() {
    return {
      placeholder: placeholder,
      // Remove the 'blogs' data property since it's now received as a prop
      bgs:[bg1,bg2,bg3,bg4,bg5,bg6],
    };
  },
  computed: {

    lang() {
      return this.$store.state.lang;
    }
  },
  methods: {
    getImageUrl(imageSrc) {

      return `${process.env.VUE_APP_BACKEND_URL}${imageSrc}`;
    },
    getBackgroundStyle(blog, index) {
      return {
        backgroundImage: `url(${this.bgs[index]})`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        backgroundSize: 'cover',
      }
    },
  },
}
</script>

<style scoped >
.latest-release {
  height: auto;
  padding: 15px;
  float: left;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  background: transparent;
  flex-shrink: 0;
}
.latest-release h2 {
  margin-bottom: 1rem;
  color: #f0f0f0;
  text-align: center;
  font-family: FiraSan;
  height: 2rem;
}

.blog-container{
  display: grid;
  grid-template-rows: repeat(auto-fit, minmax(16%, 1fr));
  grid-gap: 10px;
  /* height: 100vh; */
}

.blog-item {
  border: 2px solid #222222;
  border-radius: 10px;
  display: flex;
  height:18rem;
  flex-direction: column;
  align-items: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  
}

.blog-box{
  height: 100%;
  min-height: 200px;
  width: 100%;
  display: grid;
  grid-template-columns: 40% 40% 20%;
  overflow: hidden;
  box-sizing: border-box;
  padding: 5px;
  border-radius: 10px;

}
.img-wrapper{
  grid-column: 1;
  height: 96%; /* adjust as necessary */
  overflow: hidden;
  justify-items: stretch;
  align-items: stretch;
  box-sizing: border-box; 
  padding: 5px;
  position: relative;

}

.blog-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 5%;
  padding: 10px;
  border: 2px dashed #f0f0f0;
}

.blog-content {
  grid-column: 2;
  margin-left: 4%;
  color: whitesmoke;
  display:flex ;
  flex-direction: column;
  justify-content: space-between;
  align-items:  start;
  padding: 1rem;
}

h4{
  color:whitesmoke;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.summary{
  font-size: 1rem;
  color: whitesmoke;
  margin-bottom: 1rem;
  font-family: WuHun;
}
#timestamp{
  margin-bottom: 1px;
  margin-top: 1rem;  
}

.latest-release .blog-item .blog-meta {
  grid-column: 3;
  display: flex;
  flex-direction: column;
  justify-content: end;
  align-content: end;
  margin-left: 4%;
  padding: 1rem;
}
.authorname{
  color: #f0f0f0;
}
.authorname .authortag{
  color: skyblue;
}
.tags{
  color: #f0f0f0;
}
.tags .category{
  color: burlywood;
}
.latest-release .blog-item .blog-meta .jump-button:hover {
  background-color: #e0e0e0;
}
</style>