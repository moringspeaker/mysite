<template>
  <div class="login">
    <div class="login-wrapper">
      <h1 v-show="lang==='EN'" class="title">Login</h1>
      <h1 v-show="lang!=='EN'" class="title">登录</h1>
      <form v-if="lang==='EN'" @submit.prevent="login" >
        <input type="text" name="username" v-model="user.username" placeholder="Username" class="input-class" />
        <input type="password" name="password" v-model="user.password" placeholder="Password" class="input-class" />
        <button type="submit">Login</button>
        <a href="/#/register" class="register-link">Do not have an account? Register one now!</a>
      </form>
      <form v-if="lang!=='EN'" @submit.prevent="login" >
        <input type="text" name="username" v-model="user.username" placeholder="用户名" class="input-class" />
        <input type="password" name="password" v-model="user.password" placeholder="密码" class="input-class" />
        <button type="submit">登录</button>
        <a href="/#/register" class="register-link">还没有账号？注册一个！!</a>
      </form>

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
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
// import vueLive2d from 'vue-live2d'

export default {
  name:'UserLogin',
  // components:{
  //   live2d: vueLive2d,
  // },
  setup() {
    const store = useStore()
    const router = useRouter()
    const user = ref({
      username: '',
      password: '',
    })

    const login = async () => {
      try {
        await store.dispatch('login', user.value)
        // If the login was successful, this line will be executed
        await router.push(`/`)
      } catch (err) {
        // If there was an error in login, this block will be executed
        alert('Wrong Password');
      }
    }
    return { user, login }
  },
  computed:{
    lang(){
      return this.$store.state.lang;
    }
  }
}
</script>

<style scoped>
.login {
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

.login-wrapper {
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
form {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.input-class {
  display: block;
  margin-bottom: 10px;
}
button[type="submit"] {
  background-color: #333;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
}
.register-link{

}
.waifu{
  width: 500px;
  height: 500px;
  bottom: 10px;
  left: 10px;
  position: fixed;
}
.register-link {
  display: block;
  text-align: center;
  margin-top: 10px;
  color: #007BFF; /* Sets the text color */
  font-size: 16px;
  cursor: pointer; /* Changes the cursor to a hand when hovering over the link */
  position: relative; /* Allows you to use top, right, bottom, left for positioning */
  top: 5px; /* Adjusts the vertical position */
  left: 0; /* Adjusts the horizontal position */
}
</style>
