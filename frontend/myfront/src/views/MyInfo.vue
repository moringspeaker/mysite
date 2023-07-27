<template>
<MyInfoBanner :message="parentMessage" @updateMessage="updateParentMessage" />
  <div class="parallax p1">
    <h1 v-if="lang==='EN'">Education</h1>
    <h1 v-if="lang!=='EN'">教育经历</h1>
  </div>
  <div id="Education" class="segment-container">
    <div class="school">
          <div id="SC" >
            <h3 class="scu">Sichuan University</h3>
            <p class="CVschool">09/2018 - 06/2022</p>
            <p class="CVschool">Chengdu, Sichuan, China</p>
          </div>
        <div>
          <p class="CVself">BE: Computer Science and Technology</p>
          <P class="CVself">Scholarship: 2nd class individual scholarship of SCU (11/2019)</p>
        </div>
    </div>
    <div class="school">
        <div id="NY">
            <h3 class="nyu">New York University</h3>
             <p class="CVschool">09/2022 - present</p>
             <p class="CVschool">New York, NY, US</p>
        </div>
        <div>
          <p class="CVself">MS: Cybersecurity</p>
          <P class="CVself">Scholarship: Grad Sch of Engineering Schlp</p>
        </div>
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
    <div id="Skills" class="segment-container">
     <div class="leftbar">
      <div class="skillrow">
        <span class="skillname" v-if="lang==='EN'">Front-end Development</span>
        <span class="skillname" v-if="lang!=='EN'">前端开发</span>
        <div class="progress" role="progressbar" aria-label="Animated striped example" aria-valuenow="" aria-valuemin="0" aria-valuemax="100" style="width:100%; height: 20%;" >
            <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 80%"> 80%</div>
        </div>
      </div>
      <div class="skillrow">
        <span class="skillname" v-if="lang==='EN'">Back-end Development</span>
        <span class="skillname" v-if="lang!=='EN'">后端开发</span>
        <div class="progress" role="progressbar" aria-label="Animated striped example" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width:100%; height: 20%;" >
            <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 70%">70% </div>
        </div>
      </div>
      <div class="skillrow">
        <span class="skillname" v-if="lang==='EN'">Website Operations</span>
        <span class="skillname" v-if="lang!=='EN'">网站运维</span>
        <div class="progress" role="progressbar" aria-label="Animated striped example" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width:100%; height: 20%;" >
            <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 60%"> 60% </div>
        </div>
      </div>
    </div>
     
     <div class="leftbar">
      <div class="skillrow">
        <span class="skillname" v-if="lang==='EN'">ML(DeepLearning)</span>
        <span class="skillname" v-if="lang!=='EN'">机器学习(深度学习)</span>
        <div class="progress" role="progressbar" aria-label="Animated striped example" aria-valuenow="" aria-valuemin="0" aria-valuemax="100" style="width:100%; height: 20%;" >
            <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 80%"> 80%</div>
        </div>
      </div>
      <div class="skillrow">
        <span class="skillname" v-if="lang==='EN'">Data Analysis</span>
        <span class="skillname" v-if="lang!=='EN'">数据分析</span>
        <div class="progress" role="progressbar" aria-label="Animated striped example" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width:100%; height: 20%;" >
            <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 60%">60% </div>
        </div>
      </div>
      <div class="skillrow">
        <span class="skillname" v-if="lang==='EN'">Cybersecurity</span>
        <span class="skillname" v-if="lang!=='EN'">网络安全</span>
        <div class="progress" role="progressbar" aria-label="Animated striped example" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width:100%; height: 20%;" >
            <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 70%"> 70% </div>
        </div>
      </div>
    </div>
     <div id="word-cloud">
       <img src="https://i.imgur.com/3sZSHRp.png">
     </div>
    </div>
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
      showSC:false, 
    };
  },
  methods: {
    handleTouchStart(e) {
      this.startTouchX = e.touches[0].clientX;
    },
    handleTouchEnd(e) {
      this.endTouchX = e.changedTouches[0].clientX;
      this.detectSwipeLeft();
    },
    detectSwipeLeft() {
      if (this.startTouchX > this.endTouchX + 50) {  // The '50' is for swipe sensitivity
        this.showSC = true;
      }
    },
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
    handleScroll(){
      const SCpos = document.getElementById("SC").getBoundingClientRect();
      if (SCpos.top>0 && SCpos.top< window.innerHeight){
        this.showSC = true;
    } 
    },
    CVAnimation(){
      // Get the element
      const el1 = document.getElementById('SC');
      const el2 = document.getElementById('NY');

      // Create animation 
      const anim1 = [
        { transform: 'translateX(-100%)' },
        { transform: 'translateX(0)' } 
      ];

      // Animation for el2
      const anim2 = [
        { transform: 'translateX(100%)' },
        { transform: 'translateX(0)' }
      ];

      // Configuration
      const config = {
        duration: 1000,
        easing: 'ease-out',
        delay: 300 
      };
      // Create animation on element 
      const player = el1.animate(anim1, config);
      const player2 = el2.animate(anim2,config);
      // Finish callback
      player.finished.then(() => {
        el1.classList.add('visible');
      });

      // Play on DOM load
      document.addEventListener('DOMContentLoaded', () => {
        player.play();
        player2.play();
      });
    },
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);

    // Initial check
    this.handleScroll();
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
    showSC(newVal){
      console.log(newVal);
      if(newVal){
        this.CVAnimation();
      }
    },
  },
}
</script>

<style scoped>
.v-enter-active,
.v-leave-active {
  transition: opacity 1.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

/* Define the end state (element in its natural position) */

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
  
}
.p1{
  background-image: url("@/assets/BgImg/morning.png");
  color: #323232;
}
.p2{
  background-image: url("@/assets/BgImg/wave2.png");
  color: #323232;
}
.p3{
  background-image: url("@/assets/BgImg/sunrise.png");
  color: #323232;
}
.p4{
  background-image: url("@/assets/BgImg/night.png");
  color: #f0f0f0;
}

.segment-container{
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

.tbdu{
  margin: 40px;
}
.CVschool{
  text-align: center;
  font-size: 1rem;
}

.CVself{
  text-align: left;
  font-size: 1rem;
  margin-top: 20px;
}

.leftbar{
  width: 38%;
  height: 100%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: space-between;
  margin-left: 10px;
}

.skillrow{
  width: 100%;
  height: 35%;
}

.skillname{
  font-family: FiraSan;
  font-size:1rem ;
}

#word-cloud{
  width: 24%;
  height: 90%;
  position: relative;
  overflow: hidden;
  margin: 15px;
  display: flex;
  flex-direction: row;
  justify-content: end;
  align-content: center;
  
}
#word-cloud img{
  width: 100%; /* This will make the image take the full width of the div. You can adjust as needed. */
  height :auto; /* This maintains the image's aspect ratio */
  
  object-fit: cover;
}
</style>