<template>
  <div  id="banner-wrapper">
    <div  id="CV-navbar">
      <ul id="nav-ul">
        <li v-for="item in navitems" :key="item.id" class="nav-item"  >
         <button class="navbutton" @click="item.method">
           {{ item.name }}
         </button>
        </li>
      </ul>
    </div>
  <div id="avatar-container" class="img-wrapper">
      <img :src="avatar" alt="User Avatar" class="rounded-avatar" ref="avatarImg">
  </div>
    <div class="lower-container">
      <h2 class="myname">Chenyu</h2>
      <div class="phase-container">
        <p>Gatsby believed in the green light, the orgastic future that year by year recedes before us. It eluded us then, but that’s no matter—tomorrow we will run faster, stretch out our arms farther.... And one fine morning—— So we beat on, boats against the current, borne back ceaselessly into the past.</p>
        <p>在人生的每个阶段，我们都对漫漫前程抱着一份激动的希望，以为奇迹就在前方。然而，人生只是一个个梦想不断破灭的过程。而当我们走出所有曲折的日子时才发现，真正的美好与神奇，已经永远地留在了背后。</p>
      </div>
      <ul id="icon-list">
        <li v-for="icon in icons" :key="icon.id" class="icon-item">
          <a :href="icon.link" target="_blank" rel="noopener noreferrer">
            <img :src="icon.src" :alt="icon.name" class="icon-image">
          </a>
        </li>
      </ul>
      <div class="download-container">
        <a href="/CV/ENCV.pdf" download="My_CV.pdf" class="download-button">Download my CV</a>
        <a href="/CV/ENCV.pdf" download="我的简历.pdf" class="download-button">下载我的简历</a>
      </div>
    </div>
    <div class="arrow-down">
      <img :src="downarrow" class="arrows" :style="{ opacity: svgOpacity }" @click="DownScroll" ref="arrowsvg">
    </div>
  </div>
</template>

<script>

import avatar from '@/assets/BgImg/avatar.png'
import { useRouter } from 'vue-router'
import github from '@/assets/icons/github.svg'
import qq from '@/assets/icons/qq.svg'
import wechat from '@/assets/icons/wechat.svg'
import email from '@/assets/icons/email.svg'
import linkedin from '@/assets/icons/linkedin.svg'
import downarrow from '@/assets/icons/down-arrow.svg'

export default {
  name: "site-banner",
  props: {
    scrollTo: String,
  },
  data(){
    return {
      showBorder: false,
      pageloaded:false,
      downarrow,
      avatar,
      github,
      qq,
      wechat,
      email,
      linkedin,
      icons: [
        { id: 1, name: 'Icon 1', src: github, link: 'https://link1.com' },
        { id: 2, name: 'Icon 2', src: qq, link: 'https://link2.com' },
        { id: 3, name: 'Icon 3', src: wechat, link: 'https://link3.com' },
        { id: 4, name: 'Icon 4', src: linkedin, link: 'https://link4.com' },
        { id: 5, name: 'Icon 5', src: email, link: 'https://link4.com' },
      ],
      navitems:[
        { id: 1, name: "Home Page", method:this.GoHomePage},
        { id: 2, name: "Education", method:this.GoEducation},
        { id: 3, name: "Skills" , method:this.GoSkills},
        { id: 4, name: "Experience", method:this.GoExp },
        { id: 5, name: "Interests", method:this.GoInterests },
        { id: 6, name: "EN/中文", method:this.SetLang},
      ],
      borderOpacity: 0.8,
      svgOpacity:1,
      direction:-1,
      borderWidth: 0, // start with 10px, adjust if necessary
      blink:-1,
      currentLang:'EN',
      animationInterval: null,
    }
  },
  setup(){
    const router = useRouter();
    return {
      router
    };
  },
  computed:{
    lang(){
      return this.$store.state.lang;
    },
  },
  mounted() {
    this.pageloaded = true;
    this.startAnimation();
  },
  methods:{
    startAnimation(){
      const duration = 2000; // 2 seconds
      const stepInterval = 20; // How often to update the opacity, adjust if necessary
      const stepO = stepInterval / duration;
      const stepW = stepInterval / duration * 60;
      this.animationInterval = setInterval(()=>{
        this.borderOpacity += stepO * this.direction;
        this.borderWidth += -1 * stepW * this.direction
        this.setBorderOpacityAndWidth();
        if(this.borderOpacity <=0 ){
          this.borderOpacity = 0.8;
          this.borderWidth = 0;
        }
      },30);
       this.blinkInterval = setInterval(()=>{
        this.svgOpacity += 0.2 * this.blink;
        if(this.svgOpacity <=0  || this.svgOpacity >=1){
          this.blink = -1 * this.blink;
        }
      },150);
    },
    setBorderOpacityAndWidth(){
      let validOpacity = this.borderOpacity;
      let validWidth = this.borderWidth;
      if (this.$refs.avatarImg) {
        this.$refs.avatarImg.style.borderWidth = `${validWidth}px`;
        this.$refs.avatarImg.style.borderColor = `rgba(140, 192, 222, ${validOpacity})`;
      }

    },
    GoHomePage(){
      this.router.push('/');
    },
    GoEducation(){
      const newMessage = 'Education';
      this.$emit('updateMessage', newMessage);
    },
    GoSkills(){
      const newMessage = 'Skills';
      this.$emit('updateMessage', newMessage);
    },
    GoExp(){
      const newMessage = 'Experience';
      this.$emit('updateMessage', newMessage);
    },
    GoInterests(){
      const newMessage = 'Interests';
      this.$emit('updateMessage', newMessage);
    },
    SetLang(){
      console.log(this.currentLang);
      if (this.currentLang==='EN') {
        this.$store.commit("setLanguage", "CH");
        this.currentLang = 'CH';
      }
      else {
        this.$store.commit('setLanguage', 'EN');
        this.currentLang = 'EN';
      }
    },
    DownScroll(){
      const newMessage = 'Education';
      this.$emit('updateMessage', newMessage);
    },
  },
  watch:{
    lang(newLang){
      if (newLang==='CH'){
        this.navitems=[
          { id: 1, name: "主页", method:this.GoHomePage },
          { id: 2, name: "教育经历", method:this.GoEducation },
          { id: 3, name: "技能" , method:this.GoSkills },
          { id: 4, name: "研究经历", method:this.GoExp },
          { id: 5, name: "兴趣爱好", method:this.GoInterests },
          { id: 5, name: "中文/EN", method:this.SetLang },
        ];
      }
      else{
        this.navitems=[
          { id: 1, name: "Home Page", method:this.GoHomePage},
          { id: 2, name: "Education", method:this.GoEducation},
          { id: 3, name: "Skills" , method:this.GoSkills},
          { id: 4, name: "Experience", method:this.GoExp },
          { id: 5, name: "Interests", method:this.GoInterests },
          { id: 6, name: "EN/中文", method:this.SetLang},
        ];
      }
    }
  },
  beforeUnmount() {
    clearInterval(this.animationInterval);
  }

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

a{
  text-decoration: none;
}

#banner-wrapper {
  display: grid;
  grid-template-rows: 10% 35% 45% 10%;
  width: 100%; /* Assuming you want the banner to span the full width of its container */
  height: 100vh; /* Assuming you want the banner to span the full viewport height */
  background-image: url("@/assets/BgImg/beach.png");
  /* Center and scale the background image */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  overflow: hidden;
  box-sizing: border-box;
  border-bottom: 1rem solid #323232; /* Add this line for the black bottom border */

}

#CV-navbar {
  display: flex;
  justify-content: center; /* This will distribute your buttons more sparsely */
  align-items: center; /* This will center the buttons vertically */
}

#nav-ul ul {
  display: flex;
  gap: 1rem; /* You can adjust this value to increase/decrease space between buttons */
  padding: 0; /* To remove any default padding */
  margin: 0; /* To remove any default margin */
}
#nav-ul li:first-child {
  margin-right: 30vw;
}
.nav-item {
  list-style-type: none; /* To remove bullet points */

}

.navbutton {
  list-style: none;
  background-color: transparent;
  border: none;
  cursor: pointer;
  padding: 0.5rem 1rem; /* You can adjust this value to control button padding */
  color: #f0f0f0;
  font-size: 1.5rem;
  margin: 0 15px;  /* Adding horizontal margin for more spacing between buttons */
  transition: background-color 0.3s ease; /* Smooth transition for hover effect */
  font-weight: bolder;
}
.nav-item{
  display: inline;
}
.navbutton:hover {
  background-color: rgba(240, 240, 240, 0.5); /* This makes the button's background slightly visible (10% opacity) when hovering */
}

.img-wrapper{
  grid-row-start: 2;
  grid-row-end: 3;
  width: 100%;
  color: #f0f0f0;
  padding: 10px;
  overflow: hidden;
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.rounded-avatar {
  height: 80%;
  width: auto;
  border-radius: 50%;
  object-fit: cover;
  border: 20px solid rgba(0, 255, 255, 0.1);
  box-sizing: content-box;
}
.lower-container{
  /* margin-top: 2rem; */
  grid-row: 3/4;
  display: flex;
  flex-direction: column;
  justify-content: stretch;
  align-content: center;
  justify-items: center;
  align-items: center;
}
.myname{
  margin-top: 0px;
 color: #f0f0f0;
}
.phase-container{
  width: 60%;
  justify-content: center;
  align-items: center;
  font-size: 1.2rem;
  color: #f0f0f0;
}
#icon-list {
  display: flex;
  justify-content: center;
  gap: 2rem; /* Adjust the gap as needed */
  padding: 0;
  margin: 0.3rem 0 0; /* Add some top margin to separate from the avatar */
}

.icon-item {
  list-style-type: none;
}

.icon-image {
  width: 2rem; /* Adjust the icon size as needed */
  height: 2rem;
  transition: opacity 0.8s ease;
}

.icon-image:hover {
  opacity: 0.7; /* Opacity effect on hover */
}
.download-container{
  margin-top: 3%;
  margin-bottom: 10px;
}
.download-button{
  margin: 10px;
  border-radius: 5px;
  font-size: 1rem;
  color: #f0f0f0;
  background-color: #8CC0DE;
  border: 2px solid #323232;
  box-shadow: 0 4px 8px 2px rgba(0, 0, 0, 0.1);
  padding: 3px;
}
.arrow-down{
  grid-row: 4/5;
  background-color: #323232;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: end;
  align-items: center;
}
.arrows{
  height: 80%;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: bottom center;
  background-size: cover;
}
</style>