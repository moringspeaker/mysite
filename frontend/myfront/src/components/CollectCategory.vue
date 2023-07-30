<template>
  <div class="side-bar-container">
    <h3 v-if="lang==='EN'"  class="side-bar-header"> Blog Categories</h3>
    <h3 v-if="lang!=='EN'" class="side-bar-header"> 博客分类 </h3>
    <div class="aside-content" v-if="lang==='EN'">
      <ul v-for="(content, category) in categories" :key="category" class="side-bar-ul">
        <li  class="category-item">
          <p class="category-title">{{ category }}</p>
          <i class="bi bi-caret-down expand-icon"
             :class="expandedCategory === category ? 'fas fa-chevron-up' : 'fas fa-chevron-down'"
             @click="toggleExpand('expandedCategory',category)"
             >
            </i>
        </li>
        <ul v-if="expandedCategory === category" class="blogs-list">
          <li v-for="blog in content" :key="blog.id">
            <a :href="'/#/blogs/' + blog.id">{{blog.ENtitle}}</a>
          </li>
        </ul>
      </ul>
    </div>
    <div class="aside-content" v-if="lang!=='EN'">
      <ul v-for="(content, category) in categories" :key="category" class="side-bar-ul">
        <li  class="category-item">
          <p class="category-title">{{ category }}</p>
          <i class="bi bi-caret-down expand-icon"
             :class="expandedCategory === category ? 'fas fa-chevron-up' : 'fas fa-chevron-down'"
             @click="toggleExpand('expandedCategory',category)"
          >
          </i>
        </li>
        <ul v-if="expandedCategory === category" class="blogs-list">
          <li v-for="blog in content" :key="blog.id">
            <a :href="'/#/blogs/' + blog.id">{{blog.CHtitle}}</a>
          </li>
        </ul>
      </ul>
    </div>
     <h3 v-if="lang==='EN'"  class="side-bar-header"> Blog Collections</h3>
     <h3 v-if="lang!=='EN'" class="side-bar-header"> 博客合集 </h3>
     <div class="aside-content" v-if="lang==='EN'">
      <ul v-for="(content, collect) in collections" :key="collect" class="side-bar-ul">
        <li  class="collect-item">
          <p class="collect-title">{{ collect }}</p>
          <span class="collect-tag">{{ content.category }}</span>
          <i class="bi bi-caret-down expand-icon"
             :class="expandedCollect === collect ? 'fas fa-chevron-up' : 'fas fa-chevron-down'"
             @click="toggleExpand('expandedCollect',collect)"
          >
          </i>
        </li>
        <ul v-if="expandedCollect === collect" class="blogs-list">
          <li v-for="blog in content.blogs" :key="blog.id">
            <a :href="'/#/blogs/' + blog.id">{{blog.ENtitle}}</a>
          </li>
        </ul>
      </ul>
    </div>
    <div class="aside-content" v-if="lang!=='EN'">
      <ul v-for="(content, collect) in collections" :key="collect" class="side-bar-ul">
        <li  class="collect-item">
          <p class="collect-title">{{ collect }}</p>
          <span class="collect-tag">{{ content.category }}</span>
          <i class="bi bi-caret-down expand-icon"
             :class="expandedCollect === collect ? 'fas fa-chevron-up' : 'fas fa-chevron-down'"
             @click="toggleExpand('expandedCollect',collect)"
          >
          </i>
        </li>
        <ul v-if="expandedCollect === collect" class="blogs-list">
          <li v-for="blog in content.blogs" :key="blog.id">
            <a :href="'/#/blogs/' + blog.id">{{blog.CHtitle}}</a>
          </li>
        </ul>
      </ul>
    </div>
  </div>
</template>

<script>
import instance from "@/utils/request";

export default {
  name: "CollectCategory",
  data(){
    return{
      categories:'',
      collections:'',
      expandedCategory: null,
      expandedCollect: null,
    }
  },
  methods:{
    toggleExpand(varName,value) {
      if (this[varName] === value) {
        this[varName] = null;  // Collapse if already expanded
      } else {
        this[varName] = value;  // Expand the clicked category
      }
    }
  },
  async mounted() {
    try {
      const response = await instance.get(`${process.env.VUE_APP_BACKEND_URL}api/collectcategory/`);
      this.categories = response.data.category;
      this.collections = response.data.collection;
      console.log(this.collections);
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
  padding:5px;
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
  margin-top: 1vh;
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

.category-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.category-title {
  flex-grow: 1; /* This allows the title to take up any available space, pushing the icon to the right */
}

.collect-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.collect-title {
  flex-grow: 1; /* This allows the title to take up any available space, pushing the icon to the right */
}

.expand-icon {
  cursor: pointer;
  color: #D8D8D8;
  font-size: 20px;
  transition: color 0.3s ease;
  margin-left: 10px; /* Adds a bit of space between the title and the icon */
}

.expand-icon:hover {
  color: #393646;
}

.blogs-list {
  margin-top: 5px;
  padding-left: 10px; /* To give a slight indentation to the list */
  color: #fff3cd;
}

.collect-tag {
  margin-left: 10px;    /* Add some space between the title and the tag */
  font-size: 0.8em;     /* Make it a bit smaller than the title */
  color: #FFAA33;       /* Change the color to whatever suits your design */
  border: 1px solid #FFAA33;
  border-radius: 5px;   /* Give it rounded corners */
  padding: 2px 5px;     /* Some padding for aesthetics */
  float:right;
}
</style>