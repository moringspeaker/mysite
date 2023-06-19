<template>
  <div class="latest-release col-md-8">
    <h2 v-show="lang==='EN'">Latest Release</h2>
    <h2 v-show="lang!=='EN'">最新发布</h2>
    <div class="blog-container">
      <div class="blog-item" v-for="(blog, index) in blogs" :key="index" @click="goToBlogPage(blog.id)">
        <div class="blog-box d-flex">
         <div class="col-md-5 img-wrapper" >
           <img class="blog-image" :src="getImageUrl(blog.cover)" :alt="placeholder">
         </div>
          <div class="blog-content" v-show="lang==='EN'">
            <h4>{{ blog.ENtitle }}</h4>
            <p class="summary">{{ blog.ENsummary }}</p>
            <p class="authorname"> Created by:<span class="badge bg-secondary ">{{ blog.ENauthor }}</span></p>
            <p class="tags">tags:<span class="badge bg-secondary category"> {{ blog.category }}</span></p>
            <p class="created-date block-display" id="timestamp">{{ blog.created_date }}</p>
          </div>
          <div class="blog-content" v-show="lang!=='EN'">
            <h4>{{ blog.CHtitle }}</h4>
            <p class="summary">{{ blog.CHsummary }}</p>
            <p class="authorname"> Created by:<span class="badge bg-secondary ">{{ blog.CHauthor }}</span></p>
            <p class="tags">tags:<span class="badge bg-secondary category"> {{ blog.category }}</span></p>
            <p class="created-date block-display" id="timestamp">{{ blog.created_date }}</p>
          </div>
          <div class="blog-meta" v-show="lang==='EN'">
            <button class="btn btn-primary jump-button" @click="goToBlogPage(blog.id)">Read...</button>
          </div>
          <div class="blog-meta" v-show="lang!=='EN'">
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
  background-color: #222222;
  /*border-radius: 25px;*/
  padding: 20px;
  margin: 3vh;
  width:70%;
  float: left;
  margin-left: 20px;
  /*border: 2px solid #222222;*/

}

.blog-box {
  flex-shrink: 0;
  overflow: hidden;
  display: flex;
  /*align-items: center;*/
  gap: 20px; /* adjust this as per your need */
  /*justify-content: center;*/
}

.img-wrapper{
  height: 19rem;
  width: 24rem;
  margin: 0.8rem;
  border-radius: 5%;
  position: relative;
}

.img-wrapper:after{
  content: "";
  position: absolute;
  right: -10px;        /* position line to the right of img-wrapper */
  top: 0;             /* align to top of img-wrapper */
  height: 80%;       /* match height of img-wrapper */
  width: 1px;         /* line width */
  background: whitesmoke;  /* line color */
}

.blog-image {
  width: 100%; /* adjust this as per your need */
  height: 100%;
  object-fit: cover;
  border-radius: 5%;
}

.blog-content {
  flex-grow: 1;
  color: whitesmoke;
}

.latest-release h2 {
  margin-bottom: 1rem;
  color: #f0f0f0;
}

.latest-release .blog-item {
  margin: 1%;
  /*border: 2px solid #222222;*/
  background-color: #2C3333;
  height: 25vh;
}

.latest-release .blog-item h4 {
  font-size: 1.5rem;
  margin-top: 10%;
}

.latest-release .blog-item .summary {
  margin-top: 10%;
  color: #88ffcc;
}

.latest-release .blog-item .author {
  margin-bottom: 5px;
  color: aqua;
  margin-top: 1rem;
}

.latest-release .blog-item .category {
  margin: 10px;
  color: dodgerblue;
  margin-top: 1rem;
}

.block-display {
  display: block;
  margin-top: 1rem;
}

.latest-release .blog-item .blog-meta {
  display: flex;
  align-items: center;
}

.btn-primary.jump-button {
  background-color: lightblue; /* Change background color to light blue */
  padding: 15px 25px; /* Increase button size by adding padding */
  font-size: 18px; /* Increase font size */
  border: none; /* Remove default border */
  margin-right: 10px;
  margin-top: 15rem;
}


.latest-release .blog-item .blog-meta .jump-button:hover {
  background-color: #e0e0e0;
}
</style>