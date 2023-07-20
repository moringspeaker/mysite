<template>
<MyInfoBanner :message="parentMessage" @updateMessage="updateParentMessage" />
  <div class="parallax p1">
    <h1 v-if="lang==='EN'">Education</h1>
    <h1 v-if="lang!=='EN'">教育经历</h1>
  </div>
  <div id="Education" class="Edcontainer">
    <div class="school">
      <transition>
          <div id="SC">
            <h3 class="scu">Sichuan University</h3>
          </div>
      </transition>
        <div>Computer Science</div>
    </div>
    <div class="school">
      <transition>
        <div id="NY">
            <h3 class="nyu">New York University</h3>
          </div>
      </transition>
        <div>Cybersecurity</div>
    </div>
    <div class="TBC">
      <h3 class="tbdu">TBC...</h3>
      <h3 class="tbdu">未完待续。。。</h3>
    </div>
  </div>
  <div class="parallax p2"> 
    <h1 v-if="lang==='EN'" id="Skills">Professional Skills</h1>
    <h1 v-if="lang!=='EN'" id="Skills">职业技能</h1>
   </div>

    <h1 id="Skills">Professional Skills</h1>

  <div class="parallax p3">
    <h1 v-if="lang==='EN'" id="Experience">Work and Research Experience</h1>
    <h1 v-if="lang!=='EN'" id="Experience">研究经历</h1>
  </div>
  
    <h1 id="Experience">Work and Research Experience</h1>
  
  <div class="parallax p4">
    <h1 v-if="lang==='EN'" id="Interests">Interests</h1>
    <h1 v-if="lang!=='EN'" id="Interests">兴趣爱好</h1>
  </div>
    

    <h1 >Interests</h1>

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
      parentMessage: '',
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
   computed:{
     lang(){
      return this.$store.state.lang
    }
  },
  watch: {
    parentMessage(newValue) {
      this.scrollToHeader(newValue);
    },
     lang(newLang, oldLang) {
      if (newLang !== oldLang) {
        console.log(this.lang);
      }
  },
  },

}
</script>

<style scoped>
.v-enter {
  transform: translateX(-100%);
  opacity: 0;
}

/* Define how the transition should behave (duration, timing function, etc.) */
.v-enter-active {
  transition: transform 0.5s ease-out, opacity 0.5s ease-out;
}

/* Define the end state (element in its natural position) */
.v-enter-to {
  transform: translateX(0);
  opacity: 1;
}
.parallax{
  width: 100%;
  height: 80vh;
  position: relative;
  overflow: hidden;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: top center;
  background-attachment: fixed;
  display: flex;
  justify-content: center; /* horizontally center */
  align-items: center;  
  color: #323232;
}
.p1{
  background-image: url("@/assets/BgImg/morning.png");
}
.p2{
  background-image: url("@/assets/BgImg/wave2.png");
}
.p3{
  background-image: url("@/assets/BgImg/sunrise.png");
}
.p4{
  background-image: url("@/assets/BgImg/night.png");
}

.Edcontainer{
  height: 40vh;
  background-color: #323232;
  color: azure;
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-content: center;
}
.school{
  height: 95%;
  width: 40%;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  /* padding-left: 2rem; */
  border: #f0f0f0 2px dashed;
  margin: 10px;
  border-radius: 5px;
}

#SC{
  background-color: #ba2a17;
  color: #f0f0f0;
  height: 40%;
  width: 100%;
  justify-items: center;
  align-items: center;
}
#SC .scu{
  margin-top: 20px;
  text-align: center;
}

#NY{
  background-color: #57068c;
  color: #f0f0f0;
  height: 40%;
  width: 100%;
  justify-items: center;
  align-items: center;
}
#NY .nyu{
  margin-top: 20px;
  text-align: center;
}

.TBC{
  height: 95%;
  width: 20%;
  display: flex;
  flex-direction: column;
  justify-items: center;
  align-items: center;
  /* padding-left: 2rem; */
  border: #f0f0f0 2px dashed;
  margin: 10px;
  border-radius: 5px;
}
</style>