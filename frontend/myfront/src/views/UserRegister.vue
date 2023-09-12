<template>
  <div class="login">
    <div class="login-wrapper">
      <h1 v-show="lang==='EN'" class="title">Register</h1>
      <h1 v-show="lang!=='EN'" class="title">注册</h1>
      <form v-if="lang==='EN'" @submit.prevent="register">
        <input type="text" name="username" v-model="user.username" placeholder="Username" class="input-class" />
        <input type="text" name="email" v-model="user.email" placeholder="Your@Email.com" class="input-class" />
        <input type="password" name="password" v-model="user.password1" placeholder="Password" class="input-class" />
        <input type="password" name="password" v-model="user.password2" placeholder="Confirm Password" class="input-class" />
        <button type="submit">Register</button>
        <a href="/#/login" class="register-link">Already have an account? Log in now ~</a>
      </form>
      <form v-if="lang!=='EN'" @submit.prevent="register">
        <input type="text" name="username" v-model="user.username" placeholder="用户名" class="input-class" />
        <input type="text" name="email" v-model="user.email" placeholder="邮箱地址" class="input-class" />
        <input type="password" name="password" v-model="user.password1" placeholder="密码" class="input-class" />
        <input type="password" name="password" v-model="user.password2" placeholder="确认密码" class="input-class" />
        <button type="submit">提交</button>
        <a href="/#/login" class="register-link">已经又账户了？在这里登录 ~</a>
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
// import vueLive2d from 'vue-live2d'
import {ref} from 'vue'
import instance from "@/utils/request";
import {useRouter} from "vue-router";

export default {
  name:'UserRegister',
  // components:{
  //   live2d: vueLive2d,
  // },
  setup() {
    const router = useRouter();
    const user = ref({
      username: '',
      email: '',
      password1: '',
      password2: '',
      confirmPassword: ''
    });
    const register = async ()=> {
      // Validate email format
      const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
      if (!emailRegex.test(user.value.email)) {
        alert('Invalid email format!');
        return
      }
    let response_f = null ;
    if (user.value.password1!== user.value.password2) {
      alert('Passwords do not match!');
      return
    }
    //validate user name's length
      if (user.value.username.length < 5 || user.value.username.length > 20) {
        alert('Username must be between 5 and 20 characters long!');
        return;
      }

      // Validate email and password length
      if (user.value.email.length > 100) {
        alert('Email should not be more than 100 characters!');
        return;
      }
      if (user.value.password1.length > 100) {
        alert('Password should not be more than 100 characters!');
        return;
      }

     try {
      const response = await instance.post (`${process.env.VUE_APP_BACKEND_URL}api/user/register/`,{
         username: user.value.username,
         email: user.value.email,
         password: user.value.password1,
      })
       response_f = response;
       if (response.status === 201) {
         alert('Register Success!');

         await router.push(`/login/`);// Redirect to login
       }

     }
    catch(error) {
      alert(response_f.data);
      }
    }
      return {user, register}

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
  align-items: center; /* Aligns child elements vertically */
  justify-content: center; /* Aligns child elements horizontally */
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
