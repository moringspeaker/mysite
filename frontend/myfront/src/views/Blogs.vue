<template>
  <div class="content-wrapper">
    <blog-window :lang="lang" :blogs="blogs"/>
    <about-me :lang="lang" />
    <AudioPlayer/>
  </div>

</template>

<script>
import BlogWindow from "@/components/BlogWindow.vue";
import AboutMe from "@/components/AboutMe.vue";
import AudioPlayer from "@/components/AudioPlayer.vue";

export default {
  name: "MyBlogs",
  components: {
    BlogWindow,
    AboutMe,
    AudioPlayer,
  },
}
</script>

<style scoped>

</style>