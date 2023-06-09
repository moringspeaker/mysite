<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
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
            <a class="nav-link" :href="item.link">{{ item.name }}</a>
          </li>
        </ul>
      </div>
      <div class="dropdown ">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="languageDropdown" data-bs-toggle="dropdown" aria-expanded="false" @click="toggleDropdown">
          <i class="bi bi-translate"></i> {{ selectedLanguage }}
        </button>
        <ul v-show="isDropdownOpen" class="dropdown-menu dropdown-menu-lg-start" >
          <li v-for="(language, index) in languages" :key="index">
            <a class="dropdown-item" href="#" @click="selectLanguage(language)">
              <i class="bi bi-translate"></i> {{ language }}
            </a>
          </li>
        </ul>
      </div>
  </nav>
</template>

<script>

import avatar from '@/assets/BgImg/avatar.png';

export default {
  name: 'Nav-bar',
  data(){
    return{
      avatarUrl:avatar,
      isDropdownOpen: false, // Track the dropdown state
      languages: ['EN', '中文'], // Replace with your desired language options
      selectedLanguage: 'EN' ,  // Set the default selected language
      navitems:[
        { id: 1, name: "Home Page", link:"#" },
        { id: 2, name: "Blogs", link:"#" },
        { id: 3, name: "Publications" , link:"#"},
        { id: 4, name: "My Resource", link:"#"},
        { id: 5, name: "About Me", link:"#"},
        {id: 6, name: "Gallery", link:"#"}
      ],
    };
  },
  methods: {
    selectLanguage(language) {
      this.selectedLanguage = language;

      //send this language selection to whole project
      this.$emit("SelectLan",this.selectedLanguage);

      this.isDropdownOpen = false;
      let navitems1=[
        { id: 1, name: "Home Page", link:"#" },
        { id: 2, name: "Blogs", link:"#" },
        { id: 3, name: "Publications" , link:"#"},
        { id: 4, name: "My Resource", link:"#"},
        { id: 5, name: "About Me", link:"#"},
        {id: 6, name: "Gallery", link:"#"}
      ];
      let   navitems2=[
        { id: 1, name: "主页", link:"#" },
        { id: 2, name: "博客", link:"#" },
        { id: 3, name: "出版" , link:"#"},
        { id: 4, name: "我的资源", link:"#"},
        { id: 5, name: "关于我", link:"#"},
        {id: 6, name: "我的瞬间", link:"#"}
      ];
      if(this.selectedLanguage === "EN"){
        this.navitems = navitems1
      }
      else{
        this.navitems = navitems2
      }
    },
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen; // Toggle the dropdown state
    }
  }
};
</script>

<style scoped>
/* Add any styles here if necessary */

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
