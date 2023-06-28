 <template>
     <el-menu
         default-active="2"
         class="side-bar"
         :collapse="isCollapse"
         @open="handleOpen"
         @close="handleClose"
         text-color="#fff"
         active-text-color="#ffd04b"
         background-color="#222222"

     >
       <el-sub-menu v-for="(content, category) in blogdata.category" :key="category" :index="category" class="category-sub" v-show="lang==='EN'">
         <template #title>{{ category }}</template>    <!-- this is the categories's names-->
         <el-menu-item-group  v-for="(blog,index) in content" :key="blog" :index="index.toString()" class="blog-group" >
            <router-link :to="`/blogs/${blog.id}`" style="text-decoration: none;">
              <el-menu-item>{{ blog.ENtitle }}</el-menu-item>
            </router-link>
         </el-menu-item-group>
       </el-sub-menu>
       <div class="title-container" v-show="lang==='EN'">
         <p class="collection-title">Blog Collections</p>
       </div>
       <el-sub-menu v-for="(items, collect) in collection_list" :key="collect" :index="collect" class="collection-group" v-show="lang==='EN'">
         <template #title>{{ collect }}</template>
         <el-sub-menu v-for="(blogs, key) in items" :key="key" :index="key" class="collection-sub"  text-color="#fff" active-text-color="#ffd04b" >
           <template #title>{{ key }}</template>
           <el-menu-item v-for="(blog, index) in blogs" :key="index" :index="index.toString()" class="blogs-collection">
                          <router-link :to="`/blogs/${blog.id}`" style="text-decoration: none;">
                            <el-menu-item class="my-custom-menu-item">{{ blog.ENtitle }}</el-menu-item>
                          </router-link>
           </el-menu-item>
         </el-sub-menu>
       </el-sub-menu>

       <el-sub-menu v-for="(content, category) in blogdata.category" :key="category" :index="category" class="category-sub" v-show="lang!=='EN'">
         <template #title>{{ category }}</template>    <!-- this is the categories's names-->
         <el-menu-item-group  v-for="(blog,index) in content" :key="blog" :index="index.toString()" class="blog-group" >
           <router-link :to="`/blogs/${blog.id}`" style="text-decoration: none;">
             <el-menu-item>{{ blog.CHtitle }}</el-menu-item>
           </router-link>
         </el-menu-item-group>
       </el-sub-menu>
       <div class="title-container" v-show="lang!=='EN'">
         <p class="collection-title">Blog Collections</p>
       </div>
       <el-sub-menu v-for="(items, collect) in collection_list" :key="collect" :index="collect" class="collection-group" v-show="lang!=='EN'">
         <template #title>{{ collect }}</template>
         <el-sub-menu v-for="(blogs, key) in items" :key="key" :index="key" class="collection-sub"  text-color="#fff" active-text-color="#ffd04b" >
           <template #title>{{ key }}</template>
           <el-menu-item v-for="(blog, index) in blogs" :key="index" :index="index.toString()" class="blogs-collection">
             <router-link :to="`/blogs/${blog.id}`" style="text-decoration: none;">
               <el-menu-item class="my-custom-menu-item">{{ blog.CHtitle }}</el-menu-item>
             </router-link>
           </el-menu-item>
         </el-sub-menu>
       </el-sub-menu>
     </el-menu>
  </template>

  <script>
    import placeholder from '@/static/placeholder.png';
    import instance from "@/utils/request";

    export default {
      name:"BlogNavbar",
      components:{
        // Markdown,
      },
      props: {
        lang: {
          type: String,
          default: "EN",
        },
      },
      data() {
        return {
          placeholder: placeholder,
          blogdata: {},
          collection_list: {},
          markdownContent: '',
        };
      },
      methods: {
        getImageUrl(imageSrc) {
          // Modify the image source URL here
          return `${process.env.VUE_APP_BACKEND_URL}${imageSrc}`;
        },
      },
      async mounted() {
        try {
          const response = await instance.get(`${process.env.VUE_APP_BACKEND_URL}blogs/api/blogs/`);
          this.blogdata = response.data;
          let collections = {};
          collections = this.blogdata.collection;
          delete  collections.default;
          let newDictionary = {};   //Collate the obtained collection data

          for (let collection in collections) {
            let category = collections[collection].pop();
            if (!newDictionary[category]) {
              newDictionary[category] = {};
            }
            newDictionary[category][collection] = collections[collection];
          }
          this.collection_list = newDictionary;
        } catch (error) {
          console.error(error);
        }
      },

    }
  </script>

  <style scoped >
  .side-bar {
    min-height: 40%;
    margin-top: 3vh;
    width: 25%;
    border-radius: 10px;
    background-color: #222222;
    display: flex;
    flex-direction: column;
  }
  .category-sub{
    background-color: #222222;
  }
  .blog-group{
    background-color: #222222;
  }
  .blogs-collection .el-menu-item {
    font-size: 20px; /* set your desired font size here */
  }
.title-container{
  height:1.5rem;
  width: 100%;
  font-size: 1rem;
  margin-top: 1rem;
  justify-items: center;
}
.collection-title{
  font-size: 1rem;
  text-align: center;
  background-color: #222222;
  color: wheat;
}
.collection-group{
  background-color: #222222;
}
.collection-sub{
  background-color: #222222;
}
.blogs-collection{
  background-color: #222222;
  height:1px;
}
  .my-custom-menu-item {
    font-size: 0.8rem !important;
    padding: 5px !important;
  }
  </style>

