<template>
  <nav class="navbar navbar-expand-lg navbar-dark custom-navbar">
    <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#mobileNavbar"
        aria-controls="mobileNavbar"
        aria-expanded="ture"
        aria-label="Toggle Navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ml-auto">
        <li v-for="item in navitems" :key="item.id" class="nav-item" >

          <router-link :to="item.link" class="nav-link" ><i :class="item.icon"></i>  {{ item.name }}</router-link>
        </li>
      </ul>
    </div>

    <div class="dropdown">
      <button v-if="lang==='EN'" class="btn btn-secondary dropdown-toggle" type="button" id="authDropdown" data-bs-toggle="dropdown" aria-expanded="false">
        Welcome, {{ username }} !
      </button>
      <button v-if="lang!=='EN'" class="btn btn-secondary dropdown-toggle" type="button" id="authDropdown" data-bs-toggle="dropdown" aria-expanded="false">
        欢迎, {{ username }} !
      </button>
      <ul v-if="lang==='EN'" class="dropdown-menu" aria-labelledby="authDropdown">
        <li v-if="isLoggedIn">
          <button class="dropdown-item" @click="logout">
            Logout
          </button>
        </li>
        <template v-else>
          <li>
            <router-link to="/login" class="dropdown-item">
              Login
            </router-link>
          </li>
          <li>
            <router-link to="/register" class="dropdown-item">
              Sign Up
            </router-link>
          </li>
          <li>
            <router-link to="/logout" class="dropdown-item">
              Logout
            </router-link>
          </li>
        </template>
      </ul>
      <ul v-if="lang!=='EN'" class="dropdown-menu" aria-labelledby="authDropdown">
        <li v-if="isLoggedIn">
          <button class="dropdown-item" @click="logout">
            Logout
          </button>
        </li>
        <template v-else>
          <li>
            <router-link to="/login" class="dropdown-item">
              登录
            </router-link>
          </li>
          <li>
            <router-link to="/register" class="dropdown-item">
              注册
            </router-link>
          </li>
          <li>
            <router-link to="/logout" class="dropdown-item">
              登出
            </router-link>
          </li>
        </template>
      </ul>
    </div>

    <div class="dropdown ">
      <button class="btn btn-secondary dropdown-toggle" type="button" id="languageDropdown" data-bs-toggle="dropdown" aria-expanded="false" @click="toggleDropdown">
        <i class="bi bi-translate"></i> {{ selectedLanguage }}
      </button>
      <ul v-show="isDropdownOpen" class="dropdown-menu dropdown-menu-lg-start" >
        <li v-for="(language, index) in languages" :key="index">
          <button class="dropdown-item" href="" @click="selectLanguage(language)">
            <i class="bi bi-translate"></i> {{ language }}
          </button>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Nav-bar',
  data(){
    return{
      isDropdownOpen: false, // Track the dropdown state
      languages: ['EN', '中文'], // Replace with your desired language options
      selectedLanguage: 'EN' ,  // Set the default selected language
    };
  },
  computed:{
    lang(){
      return this.$store.state.lang;
    },
    username(){
      let is_logged = this.$store.state.isLoggedIn;
      console.log(this.$store.state.user);
      if (is_logged){
        return this.$store.state.user;
      }
      else{
        let tmp_name = "Guest"
        return tmp_name;
      }
    },
    navitems() {
      return this.$store.state.navitems;
    }
  },
  watch: {
    username(newName, oldName) {
      console.log(`Username changed from ${oldName} to ${newName}`);
      this.user = newName;
    }
  },
  mounted() {
    if(this.lang === 'EN' )
    this.selectedLanguage = this.lang;
    else
      this.selectedLanguage = '中文';
  },
  methods: {
    selectLanguage(language) {
      let navitems1=[
        { id: 1, name: "Home Page", link:"/", icon: "bi bi-house-door" },
        { id: 2, name: "Blogs", link:"/blogs", icon: "bi bi-file-text" },
        { id: 3, name: "Publications" , link:"/publications", icon: "bi bi-journal-text" },
        { id: 4, name: "My Resource", link:"/resources", icon: "bi bi-folder" },
        { id: 5, name: "MyInfo", link:"/myinfo", icon: "bi bi-person-circle" },
        { id: 6, name: "Gallery", link:"/gallery", icon: "bi bi-images" },
        { id: 7, name: "Login", link:"/login", icon: "bi bi-box-arrow-in-right" }
      ];
      let navitems2=[
        { id: 1, name: "主页", link:"/", icon: "bi bi-house-door" },
        { id: 2, name: "博客", link:"/blogs", icon: "bi bi-file-text" },
        { id: 3, name: "出版" , link:"/publications", icon: "bi bi-journal-text" },
        { id: 4, name: "我的资源", link:"/resources", icon: "bi bi-folder" },
        { id: 5, name: "关于我", link:"/myinfo", icon: "bi bi-images" },
        {id: 6, name: "我的瞬间", link:"/gallery", icon: "bi bi-house-door"},
        {id: 7, name: "登录", link:"/login", icon: "bi bi-box-arrow-in-right" }
      ];
      if(language === "EN"){
        this.selectedLanguage = "EN";
        this.$store.commit('setLanguage', 'EN');
        this.$store.commit('setNavItems', navitems1);
        console.log(this.$store.lang);
      }
      else{
        this.selectedLanguage = "中文";
        this.$store.commit('setLanguage', 'CH');
        this.$store.commit('setNavItems', navitems2);
      }
      //send this language selection to whole project
      // this.$emit("SelectLan",this.selectedLanguage);

      this.isDropdownOpen = false;
    },
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen; // Toggle the dropdown state
    }
  }
};
</script>

<style scoped>
/* Add any styles here if necessary */
.custom-navbar {
  background-color: #323232;
}

.navbar {
  display: flex;
  justify-content: center;
  align-items: center;

}
.navbar a {
  text-decoration: none;
  position: relative;
}

.navbar a::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 2px;
  background-color: antiquewhite; /* Adjust the color as needed */
  visibility: hidden;
  transform: scaleX(0);
  transition: all 0.3s ease-in-out;
}

.navbar a:hover::after {
  visibility: visible;
  transform: scaleX(1);
}

#navbarNav{
  position: center;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;

}

ul:first-of-type {
  list-style-type: none;
  justify-content: center;
  align-items: center;
  padding: 0;

}

ul:first-of-type li {
  margin-left: 2.5rem;
  margin-right: 2.5rem;
}
ul:first-of-type li a{
  font-size: 1rem;
}

.dropdown{
  margin-right: 10%;

}
</style>