<template>
  <header>
    <site-banner :lang="language"/>
    <nav-bar @SelectLan="getLanguage"/>
  </header>

 <body>
    <div id="content" class="container-padding" >
      <div id="inner-content-wrapper" class="site-content">
        <background-particles />
      </div>
    </div>

 </body>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import SiteBanner from "@/components/sitebanner.vue";

import BackgroundParticles from "@/components/BackgroundParticles.vue"
export default {
  name: 'App',
  data(){
    return{
      language:"EN",
      cn: null
    }
  },
  methods:{
    getLanguage(data){
      this.language = data;
    }
  },
  components: {
    BackgroundParticles,
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