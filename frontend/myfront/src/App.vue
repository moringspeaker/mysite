<template>
  <site-banner />
  <nav-bar />
  <div class="container-md">
    <canvas id="canvas">

    </canvas>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import SiteBanner from "@/components/sitebanner.vue";
export default {
  name: 'App',
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
</style>
