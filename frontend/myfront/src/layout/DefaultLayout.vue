<template>
  <div >
    <header>
      <site-banner :lang="lang"/>
      <nav-bar @SelectLan="getLanguage"/>
    </header>

    <main>
      <VantaBirds class="background">
          <div id="inner-content-wrapper" class="site-content x">
            <router-view :getlang="lang" :key="$route.fullPath"/>
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
  name: 'DefaultLayout',
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
.background{
  height: 100vh;
  width: 100%;
  /*position: fixed;*/
  overflow: auto;
  display: grid;
  grid-template-rows: 1fr;
  flex-direction: column;
  justify-items: center;
  align-items: center;
}

#inner-content-wrapper{
  grid-row: 1/1;
  margin-top: 20px;
  position:relative ;
  height:100%;
  width: 100rem;
  overflow: auto;
  border: 1px solid #ccc;
  padding: 10px;
  flex-direction: column;
  align-items: center;
  box-shadow: 0 15px 15px #cccccc;
  justify-content: flex-start;
}
</style>
