<template>
  <div class="logout">
    <div class="logout-wrapper">
      <h1 v-show="lang==='EN'" class="title">Logout</h1>
      <h1 v-show="lang!=='EN'" class="title">登出</h1>
      <h3 class="bye" v-show="lang==='EN'">
        Wish to see you again! {{ username }} Bye~
      </h3>
      <p v-show="lang==='EN'" class="logout-countdown">Backing to main page in {{ countdown }} seconds.</p>
      <h3 class="bye" v-show="lang!=='EN'">
        下次再见! {{ username }} Bye~
      </h3>
      <p v-show="lang!=='EN'" class="logout-countdown">在 {{ countdown }} 秒内将回到主页.</p>
    </div>
    <!--    <live2d-->
    <!--        :style="style"-->
    <!--        :model="['Potion-Maker/Pio', 'school-2017-costume-yellow']"-->
    <!--        :direction="direction"-->
    <!--        :size="size"-->
    <!--        class="waifu"-->
    <!--    ></live2d>-->
  </div>
</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
// import vueLive2d from 'vue-live2d'

export default {
  name:'UserLogout',
  // components:{
  //   live2d: vueLive2d,
  // },
  setup(){
    const store = useStore()
    const router = useRouter()
    const countdown = ref(10);
    const logout = async () => {
      try {
        await store.dispatch('logout')
        const interval = setInterval(() => {
          countdown.value--;
          if (countdown.value <= 0) {
            clearInterval(interval);
            router.push(`/`);
          }
        }, 1000); // decrement every second
      } catch (err) {
        alert('Logout Failed!');
      }
    }
    return {
      logout,
      countdown
    };
  },
  computed:{
    lang(){
      return this.$store.state.lang;
    },
    username(){
      return this.$store.state.user;
    }
  },
  mounted() {
    this.logout();
  },

}
</script>

<style scoped>
.logout {
  width: 100vw;
  height: 100vh;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  background-image: url('@/static/violet.png');
  display: flex;
  align-items: center;
  justify-content: center;
}

.logout-wrapper {
  width: 15%;
  min-height: 22%;
  font-family: Inter;
  background: #f0f0f0;
  opacity: 0.8;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
}
.logout-countdown{
  color: #526D82;
  margin-top: 20px;
  font-size: 1.2rem;
}
form {
  display: flex;
  flex-direction: column;
  align-items: center;
}
button[type="submit"] {
  background-color: #333;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
}

</style>
