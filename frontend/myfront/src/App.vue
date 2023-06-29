<template>
  <div ia="app">
    <header>
      <site-banner :lang="lang"/>
      <nav-bar @SelectLan="getLanguage"/>
    </header>

    <main>
      <VantaBirds>
        <div id="content" class="container-padding full-height" >
          <div id="inner-content-wrapper" class="site-content x">
            <router-view :getlang="lang" :key="$route.fullPath"></router-view>
          </div>
        </div>
      </VantaBirds>
    </main>
  </div>

</template>

<script>
import VantaBirds from "@/components/BirdsBackground.vue";
import NavBar from "@/components/NavBar.vue";
import SiteBanner from "@/components/sitebanner.vue";


export default {
  name: 'App',
  data(){
    return{
      cn: null,
      getlang:'',     //  if parent component want to emit a var to child components, it should declare the method first
    }
  },
  methods:{
    getLanguage(data){
      this.$store.commit('setLanguage', data);
    }
  },
  computed: {
    // Use Vuex state as a computed property
    lang() {
      return this.$store.state.lang;
    }
  },
  components: {
    VantaBirds,
    NavBar,
    SiteBanner,
  }
}
</script>

<style>


main {
  flex-grow: 1;
}

.full-height {
  height: 100%;
}

#content {

  padding: 20px;

}

#inner-content-wrapper{

  border: 1px solid #ccc;
  padding: 10px;
  margin: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 15px 15px #cccccc;
  justify-content: flex-start;
}
</style>
