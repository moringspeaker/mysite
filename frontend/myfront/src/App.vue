<template>
  <site-banner :lang="language"/>
  <nav-bar @SelectLan="getLanguage"/>
  <div class="container-md container-padding">
    <canvas id="canvas">

    </canvas>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import SiteBanner from "@/components/sitebanner.vue";
export default {
  name: 'App',
  data(){
    return{
      language:"EN"
    }
  },
  methods:{
    getLanguage(data){
      this.language = data;
      console.log(this.language)
    }
  },
  components: {
    NavBar,
    SiteBanner,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.container-padding {
  padding: 20px;
}

#canvas{
  background: antiquewhite;
}
</style>
