<template>
  <div class="latest-release col-md-8">
    <h2>Latest Release</h2>
    <div class="blog-container">
      <div class="blog-item" v-for="(blog, index) in blogs" :key="index" @click="goToBlogPage(blog.id)">
        <div class="blog-box d-flex">
         <div class="col-md-5 img-wrapper" >
           <img class="blog-image" :src="placeholder" :alt="placeholder">
         </div>
          <div class="blog-content">
            <h3>{{ blog.title }}</h3>
            <p>{{ blog.summary }}</p>
            <span class="author">Created by: </span>
            <span class="authorname">{{ blog.author }}</span>
            <span class="created-date block-display" id="timestamp">{{ blog.createdDate }}</span>
          </div>
          <div class="blog-meta">
            <button class="btn btn-primary jump-button" @click="goToBlogPage(blog.id)">Jump</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import placeholder from '/src/static/placeholder.png'
export default {
  name: "BlogWindow",
  data(){
    return{
      placeholder:placeholder,
      ///////////////////////////blogs
      blogs: [
        {
          id: 1,
          img:"",
          title: "Blog 1",
          summary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          author: "John Doe",
          createdDate: "2023-06-01"
        },
        {
          id: 2,
          img:"",
          title: "Blog 2",
          summary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          author: "Jane Smith",
          createdDate: "2023-06-02"
        },
        {
          id: 3,
          title: "Blog 3",
          summary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          author: "Alice Johnson",
          createdDate: "2023-06-03"
        },
        {
          id: 4,
          img:"",
          title: "Blog 4",
          summary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          author: "Bob Thompson",
          createdDate: "2023-06-04"
        },
        {
          id: 5,
          img:"",
          title: "Blog 5",
          summary: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          author: "Emily Brown",
          createdDate: "2023-06-05"
        }
      ],
      //////////////////////////
    }
  },
}
</script>

<style scoped >
.latest-release {
  background-color: #222222;
  border-radius: 25px;
  padding: 20px;
  margin: 3vh;
  width:70%;
  float: left;
  margin-left: 2px;
  /*border: 2px solid #222222;*/

}

.blog-box {
  flex-shrink: 0;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 20px; /* adjust this as per your need */
  justify-content: center;
}

.img-wrapper{
  height: 19rem;
  width: 24rem;
  margin: 0.8rem;
  border-radius: 15%;
  position: relative;
}
.img-wrapper:after{
  content: "";
  position: absolute;
  right: -10px;        /* position line to the right of img-wrapper */
  top: 0;             /* align to top of img-wrapper */
  height: 100%;       /* match height of img-wrapper */
  width: 1px;         /* line width */
  background: whitesmoke;  /* line color */
}


.blog-image {
  width: 100%; /* adjust this as per your need */
  height: 100%;
  object-fit: cover;
  border-radius: 15%;
}


.blog-content {
  flex-grow: 1;
  color: whitesmoke;
}

.latest-release h2 {
  margin-bottom: 10px;
  color: #f0f0f0;
}

.latest-release .blog-item {
  margin: 1%;
  /*border: 2px solid #222222;*/
  background-color: #2C3333;
  height: 25vh;
}

.latest-release .blog-item h3 {
  font-size: 4rem;
  margin-bottom: 5px;
}

.latest-release .blog-item p {
  margin-bottom: 5px;
  color: #88ffcc;
}

.latest-release .blog-item .author {
  margin-bottom: 5px;
  color: aqua;
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
  border-radius: 15%; /* Round the corners of the button */
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