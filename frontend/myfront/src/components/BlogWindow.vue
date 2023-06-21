<template>
  <div class="latest-release ">
    <h2 v-show="lang==='EN'">Latest Release</h2>
    <h2 v-show="lang!=='EN'">最新发布</h2>
    <div class="blog-container">
      <div class="blog-item" v-for="(blog, index) in blogs" :key="index" @click="goToBlogPage(blog.id)">
        <div class="blog-box">
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
             <p class="tags">tags:<span class="badge bg-secondary category"> {{ blog.category }}</span></p>
            <button class="btn btn-primary jump-button" @click="goToBlogPage(blog.id)">Read...</button>
          </div>
          <div class="blog-meta" v-show="lang!=='EN'">
            <p class="authorname"> Created by:<span class="badge bg-secondary authortag" >{{ blog.CHauthor }}</span></p>
              <p class="tags">tags:<span class="badge bg-secondary category"> {{ blog.category }}</span></p>
            <button class="btn btn-primary jump-button" @click="goToBlogPage(blog.id)">打开...</button>
          </div> 
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import placeholder from '@/static/placeholder.png';

export default {
  name: "BlogWindow",

  props: {
    lang: {
      type: String,
      default: "EN",
    },
    blogs: {
      type: Array, // Update the type to Array
      default: function () {
        return []; // Set the default value to an empty array
      },
    },
  },

  data() {
    return {
      placeholder: placeholder,
      // Remove the 'blogs' data property since it's now received as a prop
    };
  },

  async mounted() {
    console.log(this.blogs); // Access and use the 'blogs' prop
  },

  methods: {
    getImageUrl(imageSrc) {
      // Modify the image source URL here
      console.log(`http://127.0.0.1:8000${imageSrc}`);
      return `http://127.0.0.1:8000${imageSrc}`;
    },
  },
}
</script>

<style scoped >
.latest-release {
  grid-column: 1/2;
  grid-row: 1/5;
  background-color: #222222;
  padding: 15px;
  margin-top: 3vh;
  float: left;
  /*height:100vh;*/
  border: 2px solid #222222;
}
.latest-release h2 {
  margin-bottom: 1rem;
  color: #f0f0f0;
}

.blog-container{
  height:100%;
  width: 100%;
  display:grid;
  grid-template-rows: repeat(5, 19%);
  grid-template-columns: repeat(3, 33%);
  grid-auto-flow: column dense;
}

.latest-release .blog-item {
  margin: 1%;
  border: 2px solid #222222;
  background-color: #2C3333;
  grid-column: 1/4;
}

.latest-release .blog-item .blog-box{
  height: 100%;
  width: 100%;
  display: inline-grid;
  grid-template-columns: 40% 40% 20%;
  overflow: hidden;
  grid-auto-rows: 1; 
  box-sizing: border-box;
  padding: 5px;
}
.img-wrapper{
  grid-column: 1;
  height: 96%; /* adjust as necessary */
  border-radius: 5%;
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
}
.img-wrapper:after{
  content: "";
  position: absolute;
  right: 0; /* changed this from -20px to 0 */       
  top: 0;            
  height: 100%;      
  width: 2px;         
  background: whitesmoke;    
}
.blog-content {
  grid-column: 2;
  margin-left: 4%;
  color: whitesmoke;
}

h4{
  color:#f0f0f0;
}

.summary{
  font-size: 1rem;
  color: aquamarine;
}

.latest-release .blog-item .blog-meta {
  grid-column: 3;
  align-items: flex-end;
  justify-items: center;
  margin-left: 4%;
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
.btn-primary.jump-button {
  background-color: lightblue; 
  padding: 15px 25px;
  font-size: 18px; 
  border: none; 
}


.latest-release .blog-item .blog-meta .jump-button:hover {
  background-color: #e0e0e0;
}
</style>