<template>
<MyInfoBanner :message="parentMessage" @updateMessage="updateParentMessage" />
  <div class="parallax p1"></div>
  <div>
    <h1 id="Education">Education</h1>
  </div>
  <div class="parallax p2"></div>
  <div>
    <h1 id="Skills">Professional Skills</h1>
  </div>
  <div class="parallax p3"></div>
  <div>
    <h1 id="Experience">Work and Research Experience</h1>
  </div>
  <div class="parallax p4"></div>
  <div>
    <h1 id="Interests">Interests</h1>
  </div>
</template>

<script>
import MyInfoBanner from "@/components/MyInfoBanner.vue";
export default {
  name: "AboutMe",
  components:{
    MyInfoBanner,
  },
  data() {
    return {
      parentMessage: ''
    };
  },
  methods: {
    updateParentMessage(newMessage) {
      this.parentMessage = newMessage;
    },
    scrollToHeader(id) {
      const element = document.getElementById(id);
      if (element) {
        element.scrollIntoView({
          behavior: 'smooth',
          block: 'start',
        });
      }
    },
  },
  watch: {
    parentMessage(newValue) {
      this.scrollToHeader(newValue);
    }
  },
}
</script>

<style scoped>
.parallax{
  width: 100%;
  height: 90vh;
  position: relative;
  overflow: hidden;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top center;
  background-attachment: fixed;
}
.p1{
  background-image: url("@/assets/BgImg/sunrise.png");
}
.p2{
  background-image: url("@/assets/BgImg/morning.png");
}
.p3{
  background-image: url("@/assets/BgImg/noon.png");
}
.p4{
  background-image: url("@/assets/BgImg/night.png");
}
</style>