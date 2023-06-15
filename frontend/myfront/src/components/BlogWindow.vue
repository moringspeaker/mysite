<template>
  <div class="latest-release col-md-8">
    <h2 v-show="lang==='EN'">Latest Release</h2>
    <h2 v-show="lang!=='EN'">最新发布</h2>
    <div class="blog-container">
      <div class="blog-item" v-for="(blog, index) in blogs" :key="index" @click="goToBlogPage(blog.id)">
        <div class="blog-box d-flex">
         <div class="col-md-5 img-wrapper" >
           <img class="blog-image" :src="placeholder" :alt="placeholder">
         </div>
          <div class="blog-content" v-show="lang==='EN'">
            <h3>{{ blog.ENtitle }}</h3>
            <p>{{ blog.ENsum }}</p>
            <span class="author">Created by: </span>
            <span class="authorname">{{ blog.ENauthor }}</span>
            <span class="created-date block-display" id="timestamp">{{ blog.createdDate }}</span>
          </div>
          <div class="blog-content" v-show="lang!=='EN'">
            <h3>{{ blog.CHtitle }}</h3>
            <p>{{ blog.CHsum }}</p>
            <span class="author">发布自: </span>
            <span class="authorname">{{ blog.CHauthor }}</span>
            <span class="created-date block-display" id="timestamp">{{ blog.createdDate }}</span>
          </div>
          <div class="blog-meta" v-show="lang==='EN'">
            <button class="btn btn-primary jump-button" @click="goToBlogPage(blog.id)">Jump</button>
          </div>
          <div class="blog-meta" v-show="lang!=='EN'">
            <button class="btn btn-primary jump-button" @click="goToBlogPage(blog.id)">打开</button>
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

  props: ['sentlang'],
  watch: {
    sentlang: function (data) {
      if (data === "中文") {
        data = "CH";
      }
      this.lang = data;
      console.log(this.lang)
    }
  },
  data() {
    return {
      lang: 'EN',
      placeholder: placeholder,
      ///////////////////////////blogs
      blogs: [
        {
          id: 1,
          img: "",
          ENtitle: "Blog 1",
          ENsum: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          ENauthor: "John Doe",
          CHtitle: "博客1",
          CHsum: "长风沛雨，艳阳明月，那时田野被喜悦铺满，天地间充斥着生的豪情，风力梦里也全是不屈不挠的欲望。 那时候灵魂被置于一旁，就像秋天尚且遥远，思念还未成熟。那时候视觉呈一条直线，无暇旁顾。 “这个爱情古诗，好像是个悲剧？” “你说的是婚姻，爱情没有悲剧。” 那安静，如今想来，是由于四周和心中的荒旷。一个无措的灵魂，不期而至竟仿佛走回到生命的起点。 我已不在地坛，地坛在我。\n",
          CHauthor: "史铁生",
          createdDate: "2023-06-01"
        },
        {
          id: 2,
          img: "",
          ENtitle: "Blog 2",
          ENsum: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          ENauthor: "John Doe",
          CHtitle: "博客2",
          CHsum: "我常以为是丑女造就了美人。我常以为是愚氓举出了智者。我常以为是懦夫衬照了英雄。我常以为是众人度化了佛祖。\n",
          CHauthor: "史铁生",
          createdDate: "2023-06-02"
        },
        {
          id: 3,
          ENtitle: "Blog 3",
          ENsum: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          ENauthor: "John Doe",
          CHtitle: "博客3",
          CHsum: "生命就是这样一个过程，一个不断超越自身局限的过程，这就是命运，任何人都是一样，在这过程中我们遭遇痛苦，超越局限，从而感受幸福。所以一切人都是平等的，我们毫不特殊。\n",
          CHauthor: "史铁生",
          createdDate: "2023-06-03"
        },
        {
          id: 4,
          img: "",
          ENtitle: "Blog 4",
          ENsum: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          ENauthor: "John Doe",
          CHtitle: "博客4",
          CHsum: "沉默就常常是必要的，沉默可以通向有声有形的语言所不能到达的地方。\n" +
              "\n" +
              "就像浪，舒缓下来，感悟到了水的深阔、水对浪的包容、水于浪永久的梦想意义。\n",
          CHauthor: "史铁生",
          createdDate: "2023-06-04"
        },
        {
          id: 5,
          img: "",
          ENtitle: "Blog 5",
          ENsum: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
          ENauthor: "John Doe",
          CHtitle: "博客5",
          CHsum: "我什么都没有忘，但是有些事只适合收藏，不能说，也不能想，却又不能忘。\n",
          CHauthor: "史铁生",
          createdDate: "2023-06-05"
        }
      ],
      //////////////////////////
    }
  },
  // beforeMount: {
  //   print(){
  //     console.log(this.blogs.content);
  //     },
  //   localizedBlogs() {
  //     return this.blogs.map(blog => {
  //       return {
  //         id: blog.id,
  //         img: blog.img,
  //         createdDate: blog.createdDate,
  //         content: blog[this.lang],
  //       };
  //     });
  //   },
  // },
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