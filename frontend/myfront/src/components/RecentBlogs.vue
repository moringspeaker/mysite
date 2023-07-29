<template>
  <div class="side-bar-container">
    <h3 v-if="lang==='EN'" class="side-bar-header"> Recent Blogs</h3>
    <h3 v-if="lang!=='EN'" class="side-bar-header"> 近期博客</h3>
    <div class="aside-content">
      <ul v-for="(blog,index) in recentblogs" :key="index" class="side-bar-ul">
        <li v-if="lang==='EN'">
          <a :href="'/#/blogs/' + blog.id">{{blog.ENtitle}}</a>
          <span class="blog-tag">{{blog.category}}</span>
        </li>
        <li v-if="lang!=='EN'">
          <a :href="'/#/blogs/' + blog.id">{{blog.CHtitle}}</a>
          <span class="blog-tag">{{blog.category}}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import instance from "@/utils/request";

export default {
  name: "RecentBlogs",
  data(){
    return{
      recentblogs:'',
    }
  },
  async mounted() {
    try {
      const response = await instance.post(`${process.env.VUE_APP_BACKEND_URL}api/blogs/`,{ page: 1 });
      this.recentblogs= response.data.results;
    } catch (error) {
      console.error(error);
    }
  },
  computed:{
    lang(){
     return this.$store.state.lang;
    },
  },
  watch:{
    lang(newLang){
      console.log('111111111'+newLang);
      if (newLang === "EN") {
        document.getElementById("webtitle").style.fontFamily="OribitronM";
        this.Title = "Chenyu's Website";
        this.slogan = "Live life. Learn lessons. Liberate yourself.";
      } else if (newLang !== "EN") {
        document.getElementById("webtitle").style.fontFamily="WY";
        this.Title = "尘语的网站";
        this.slogan = "宇宙以其不息的欲望将一个歌舞炼为永恒，\n" +
            "这欲望有怎样一个人间的姓名，\n" +
            "大可忽略不计。";
      }
    }
  },
}
</script>

<style scoped>


li {
  overflow-wrap: break-word;
  list-style-type: none;
  width: 100%;
  display: block;
  padding:10px;
  position: relative;
}

li::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 10px;
  right: 10px;
  height: 1px;
  opacity: 0.5;
  border-bottom: 1px dashed  #9BA4B5;
  background-size: 3px 1px;
  display:inline-block
}


li:hover {
  background-color: #444444; /* This sets a light gray background on hover */
}

.side-bar-container{
  width:100% ;
  min-height: 20%;
  margin-top: 3vh;
  border-radius: 10px;
  background-color: #222222;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  color: #f0f0f0;
  align-items: center;
}
.aside-content{
  width: 100%;
  padding: 0;
  margin: 0;
}
.side-bar-header{
  text-align: center;
  margin-top: 10px;

}

.side-bar-ul{
  width: 100%;
  padding: 0;
  margin: 0;
}

.blog-tag {
  margin-left: 10px;    /* Add some space between the title and the tag */
  font-size: 0.8em;     /* Make it a bit smaller than the title */
  color: #FFAA33;       /* Change the color to whatever suits your design */
  border: 1px solid #FFAA33;
  border-radius: 5px;   /* Give it rounded corners */
  padding: 2px 5px;     /* Some padding for aesthetics */
  float:right;
}
</style>