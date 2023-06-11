<template>
  <header>
    <site-banner :lang="language"/>
    <nav-bar @SelectLan="getLanguage"/>
  </header>

 <main>
   <VantaBirdsBackground>
     <div id="content" class="container-padding" >
       <div id="inner-content-wrapper" class="site-content">

       </div>
     </div>

   </VantaBirdsBackground>


 </main>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import SiteBanner from "@/components/sitebanner.vue";
import VantaBirdsBackground from '@/components/VantaBirdsBackground.vue';
import img from "@/assets/BgImg/MyAvatar.png"
export default {
  name: 'App',
  data(){
    return{
      language:"EN",
      cn: null,
      img:img,
    }
  },
  methods:{
    getLanguage(data){
      this.language = data;
    }
  },
  components: {
    VantaBirdsBackground,
    NavBar,
    SiteBanner,
  }
}
</script>

<style>
.container-padding {
  padding: 20px;
}


#inner-content-wrapper{
  height: 50rem;
  width: 50rem;
  margin: auto;
}
</style>