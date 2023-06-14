<template>
  <div class="latest-release">
    <h2>Latest Release</h2>
    <div class="blog-container">
      <div class="blog-item" v-for="(blog, index) in blogs" :key="index" @click="goToBlogPage(blog.id)">
        <div class="blog-box">
          <h3>{{ blog.title }}</h3>
          <p>{{ blog.summary }}</p>
          <div class="blog-meta">
            <span class="author">{{ blog.author }}</span>
            <span class="created-date">{{ blog.createdDate }}</span>
            <button class="jump-button" @click="goToBlogPage(blog.id)">Jump</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BlogWindow",
  data(){
    return{
      ///////////////////////////blogs
      blogs: [
        {
          id: 1,
          title: "Blog 1",
          summary: "Summary of Blog 1",
          author: "John Doe",
          createdDate: "2023-06-01"
        },
        {
          id: 2,
          title: "Blog 2",
          summary: "Summary of Blog 2",
          author: "Jane Smith",
          createdDate: "2023-06-02"
        },
        {
          id: 3,
          title: "Blog 3",
          summary: "Summary of Blog 3",
          author: "Alice Johnson",
          createdDate: "2023-06-03"
        },
        {
          id: 4,
          title: "Blog 4",
          summary: "Summary of Blog 4",
          author: "Bob Thompson",
          createdDate: "2023-06-04"
        },
        {
          id: 5,
          title: "Blog 5",
          summary: "Summary of Blog 5",
          author: "Emily Brown",
          createdDate: "2023-06-05"
        }
      ],
      //////////////////////////
    }
  },
}
</script>

<style scoped>
.latest-release {
  background-color: #526D82;
  border-radius: 25px;
  padding: 20px;
  margin: 3vh;
  width: 100%;
  /*border: 2px solid #222222;*/
}

.latest-release h2 {
  margin-bottom: 10px;
}

.latest-release .blog-item {
  margin: 1%;
  /*border: 2px solid #222222;*/
  background-color: #27374D;
  height: 25vh;
}

.latest-release .blog-item h3 {
  font-size: 18px;
  margin-bottom: 5px;
}

.latest-release .blog-item p {
  margin-bottom: 5px;
}

.latest-release .blog-item .blog-meta {
  display: flex;
  align-items: center;
}

.latest-release .blog-item .blog-meta .author {
  margin-right: 10px;
  font-weight: bold;
}

.latest-release .blog-item .blog-meta .created-date {
  margin-right: 10px;
  color: gray;
}

.latest-release .blog-item .blog-meta .jump-button {
  padding: 5px 10px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 4px;
  color: #333;
  cursor: pointer;
}

.latest-release .blog-item .blog-meta .jump-button:hover {
  background-color: #e0e0e0;
}
</style>