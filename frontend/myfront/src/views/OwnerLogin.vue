<template>
  <div class="login">
    <div class="login-wrapper">
      <h1 class="title">Login( if you can )</h1>
      <form @submit.prevent="login">
        <input type="text" name="username" v-model="user.username" placeholder="Username" class="input-class" />
        <input type="password" name="password" v-model="user.password" placeholder="Password" class="input-class" />
        <button type="submit">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name:'OwnerLogin',
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
        router.push(`/writeblog`)
      } catch (err) {
        // If there was an error in login, this block will be executed
        console.log(err)
      }
    }

    return { user, login }
  }
}
</script>

<style scoped>
.login {
  width: 100vw;
  height:100vh;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
background-position:center;
background-image: url('@/static/violet.png');
background-size: cover;
display: flex;
flex-direction: column;
align-items: center;
justify-items: center;
}
.login-wrapper{
width: 30%;
height:30%;
margin-top: 45vh;
margin-left: 20%;
font-family: Lobster;
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


</style>
