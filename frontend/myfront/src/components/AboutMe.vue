<template>
  <div class="about-me">
    <!-- First part: About Me text -->
    <div class="about-me__header ">
      <p class="title1" v-show="lang==='EN'">About Me</p>
      <p class="title2" v-show="lang!=='EN'">关于我</p>
    </div>

    <!-- Second part: Rotating Avatar -->
    <div class="about-me__avatar">
      <img :src="avatar" alt="Avatar" class="rotating-avatar" />
      <p v-show="lang==='EN'">Chenyu</p>
      <p v-show="lang!=='EN'">尘语</p>
    </div>

    <!-- Third part: Self Introduction -->
    <div class="about-me__intro">
      <p v-show="lang==='EN'">{{ ENintroduction }}</p>
      <p v-show="lang!=='EN'">{{ Chintroduction }}</p>
    </div>
  </div>
</template>

<script>
import avatar from '@/assets/BgImg/avatar.png'
export default {
  name: 'AboutMe',
  props:{
    lang:{
      type:String,
      default:"EN"
    }
  },
  data() {
    return {
      avatar,  // replace with your avatar url
      ENintroduction: "Welcome to my personal website! This website is mainly used for recording fun and profound technologies",  // replace with your introduction
      Chintroduction:"欢迎来到我的个人网站!本网站主要用于整理科研资料和有意思的计算机技术，以后会有更多功能，如果有任何建议，欢迎通过新建issue的方式给我留言",
    }
  }
}
</script>

<style scoped>
.about-me {
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #222222;
  border-radius: 10px;
  margin-top: 3vh;
  grid-row: 1 / 3;
  grid-column: 2 / 3;
}

.about-me__header{
  background-color: #04293A;
  color:#f0f0f0;
  width: 100%;
  height: 20%;
  display: flex;
  justify-content: center;  /* This centers the items horizontally */
  align-items: center;
  height: 20%;
  border-radius: 10px;
}
.title1{
  width: 100%;
  text-align: center;
  /*margin-left: 33%;*/
  font-size: 2rem;
}
.title2{
  width: 100%;
  /*margin-left: 40%;*/
  font-size: 2rem;
  text-align: center;
}

.about-me__avatar{
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  border-top: 2px solid antiquewhite;
  color: #f0f0f0;
  padding: 10px;
  background: url("@/static/avatar.jpg") center; /* Customize your background image */
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
.about-me__avatar p{
  font-size: 1.5rem;
  margin-top: 10px;
}

.about-me__intro {
  flex-grow: 1;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-top: 2px solid #f0f0f0;
  color: #f0f0f0;
  padding: 10px;
}

.rotating-avatar {
  width: 40%;
  border-radius: 50%;
  animation: rotation 3s infinite linear;
}

@keyframes rotation {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(359deg);
  }
}
</style>