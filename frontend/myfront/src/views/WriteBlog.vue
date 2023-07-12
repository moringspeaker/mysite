<template>
  <div class="page-container">

    <div class="head">
      <input class="en-title-input" v-model="blog.ENtitle" placeholder="Enter English title" />
      <textarea  class="en-summary-input" v-model="blog.ENsummary" placeholder="Write a summary in English"></textarea>
      <div class="cover">
        <h2 calss="title"> Write Your Blog</h2>
        <p>Choose your blog cover</p>
        <input type="file" class="coverimg" @change="onFileChange">

      </div>
      <input class="ch-title-input" v-model="blog.CHtitle" placeholder="中文标题" />
      <textarea class="ch-summary-input" v-model="blog.CHsummary" placeholder="完成中文的总结"></textarea>
    </div>
    <div class="write-page">
      <div class="md-input">
        <textarea class="content-input" v-model="blog.ENcontent" placeholder="Write your blog in markdown" v-if="lang==='EN'"></textarea>
        <textarea class="content-input" v-model="blog.CHcontent" placeholder="这是中文的博客编写页面" v-if="lang!=='EN'"></textarea>
        <button class="compile btn btn-danger btn-md" @click="switchlang()" >更换语言（当前：{{lang}}）</button>
        <button class="compile btn btn-primary btn-md" @click="compile()">Compile</button>
        <button class="compile btn btn-dark btn-md" @click="backhomepage">BackHome</button>
      </div>
      <div class="right" >
        <div  class="preview" v-html="markdown"/>
       <div class="submit">
         <el-select
             v-model="selectedCategory"
             multiple
             filterable
             allow-create
             default-first-option
             :reserve-keyword="false"
             placeholder="categories"
             v-if="categories"
         >
           <el-option
               v-for="(item,index) in categories"
               :key="index"
               :label="item.id"
               :value="item"
           />
         </el-select>
         <p>==>category</p>
         <el-select
             v-model="selectedCollection"
             multiple
             filterable
             allow-create
             default-first-option
             :reserve-keyword="false"
             placeholder="collections"
             v-if="categories"
         >
           <el-option
               v-for="(item,index) in collections"
               :key="index"
               :label="item.id"
               :value="item"
           />
         </el-select>
         <p>==>category</p>
         <date-picker @onEvent="handleDateChange" />
         <button class="submit-btn btn btn-light btn-lg" @click="submitBlog" >submit</button>
       </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import md from '@/markdownParser';
import DatePicker from "@/components/DatePicker.vue";
import { useRouter } from 'vue-router'

export default {
  data(){
    return{
      markdown: '',
      lang: 'EN',
      collections: [],
      categories: [],
      date: '',
      selectedCollection: '',
      selectedCategory: '',
    }
  },
  components:{
    DatePicker: DatePicker,
  },
  setup() {
    const blog = ref({
      ENtitle: '',
      ENcontent: '',
      ENauthor: 'Chenyu',
      ENsummary: '',
      CHtitle: '',
      CHcontent: '',
      CHauthor: '尘语',
      CHsummary: '',
      cover: null,
    })

    const onFileChange = (e) => {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      blog.value.cover = files[0];
    }
    const router = useRouter();
    return {
      blog,
      onFileChange,
      router
    }
  },
  methods: {
    handleDateChange(newDate){
      this.date = newDate;
      console.log(this.date);
    },
    async fetchCollections() {
      try {
        const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}api/collections`);
        this.collections = response.data;
        console.log(this.collections);
      } catch (err) {
        console.error(err);
      }
    },
    async fetchCategories() {
      try {
        const response = await axios.get(`${process.env.VUE_APP_BACKEND_URL}api/categories`);
        this.categories = response.data;
        console.log(this.categories);
      } catch (err) {
        console.error(err);
      }
    },
    compile() {
     if (this.lang==='EN'){
       this.markdown = md.render(this.blog.ENcontent);
     }
     else {
       this.markdown = md.render(this.blog.CHcontent);
     }
    },
    backhomepage() {

      this.router.push(`/blogs/`);
    },
    switchlang(){
      if (this.lang==='EN'){
        this.lang = 'CH';
      }
      else {
        this.lang = 'EN';
      }
    },
    async submitBlog() {
      const blogData = {
        ENtitle: this.blog.ENtitle,
        ENcontent: this.blog.ENcontent,
        ENauthor: this.blog.ENauthor,
        ENsummary: this.blog.ENsummary,
        CHtitle: this.blog.CHtitle,
        CHcontent: this.blog.CHcontent,
        CHauthor: this.blog.CHauthor,
        CHsummary: this.blog.CHsummary,
        cover: this.blog.cover,
        // Add other properties as needed
        // ...
        date: this.date,
        category: this.selectedCategory.toString(),
        collection: this.selectedCollection.toString(),
      };
      console.log(blogData);
      try {
        // Submit the blog
        const response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}api/blogwrite`, blogData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        // If successful, reset the blog form data
        if (response.status === 201) {
          this.blog.value = {
            ENtitle: '',
            ENcontent: '',
            ENauthor: 'Chenyu',
            ENsummary: '',
            CHtitle: '',
            CHcontent: '',
            CHauthor: '尘语',
            CHsummary: '',
            cover: null,
            collection: null, // you need to provide collection id
            category: null, // you need to provide category id
          };

          alert('Blog submitted successfully')
          await this.router.push(`/blogs/`);
        }
      } catch (err) {
        console.error(err)
      }
    },
  },
  mounted() {
    this.fetchCollections();
    this.fetchCategories();
  },
}
</script>

<style scoped>
.page-container{
  width: 100vw;
  height: 100vh;
  display: grid;
  grid-template-rows: 15% 85% ;
  background-image: url("@/static/starrynight.png");
  background-repeat: no-repeat;
  background-size: cover;
}
::placeholder { /* Most modern browsers support this */
  color: white; /* Change color to your preference */
}

.head{
  grid-row: 1/2;
  display: grid;
  grid-template-columns: 2fr 1fr 2fr;
  grid-template-rows: 1fr 1fr;
}
.head .en-title-input{
  grid-row: 1/2;
  grid-column: 1/2;
  background-color: transparent;
  color: mediumspringgreen;
  text-align: center;
  margin-left: 1rem;
  padding: 10px;
}
.head .en-summary-input{
  grid-row: 2/3;
  grid-column: 1/2;
  background-color: transparent;
  color: chocolate;
  margin-left: 1rem;
  padding: 10px;
}
.head .ch-title-input{
  grid-row: 1/2;
  grid-column: 3/4;
  background-color: transparent;
  color: mediumspringgreen;
  text-align: center;
  margin-right: 1rem;
  padding: 10px;
}
.head .cover{
  grid-row: 1/3;
  grid-column: 2/3;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  color: #e0e0e0;
}
.coverimg{
  margin-left: 25%;
}
.head .cover h2 {
  text-align: center;
  font-family: "Arial Black";
  font-size: 2rem;

}
.head .ch-summary-input {
  grid-row: 2/3;
  grid-column: 3/4;
  background-color: transparent;
  color: chocolate;
  margin-right: 1rem;
  padding: 10px;
}

.write-page {
  grid-row:2/3;
  display: grid;
  grid-template-columns: 1fr 1fr;

}
.write-page .md-input{
  background-color: transparent;
  border:1rem solid #fff2;
  resize: none;  /* Optional: disables resizing */
  color: #222222;
  border-radius: 20px;
  padding: 10px;
  overflow: auto;
}

.content-input{
  width: 100%;
  height: 92%;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  background-color: transparent;
  border: none;
  resize: none;  /* Optional: disables resizing */
  color: wheat;
  font-size: 1rem;
}
.md-input .compile{
  margin-top: 20px;
  margin-left: 10%;
}
.md-input {
  width: 100%;
  height: 100%;
  grid-column: 1/2;
  background-color: #f0f0f0;
}
.right{
  width: 100%;
  height: 100%;
  grid-column: 2/3;
  overflow: auto;
  border:1rem solid #fff2;
  resize: none;  /* Optional: disables resizing */
  color: aqua;
  border-radius: 20px;
  padding: 10px;
  overflow: auto;
  display: flex;
  flex-direction: column;
}
.preview{
  overflow: scroll;
  width: 100%;
  height: 90%;
}
.submit{
  width: 100%;
  height: 10%;
  border-radius: 10px;
  padding: 5px;
  justify-items: center;
  align-items: center;
  display: flex;
  gap:5px;
  color: whitesmoke;
}
</style>