<template>
  <div id="app">
      <router-view :key="$route.fullPath"/>
    <footer>
      <blog-footer :is="activeComponent"/>
    </footer>
  </div>
</template>
<script>
import BlogFooter from "@/components/BlogFooter.vue";
export default {
  name:'App',
  components:{
    BlogFooter,
  }
}
</script>

<style >

</style>
