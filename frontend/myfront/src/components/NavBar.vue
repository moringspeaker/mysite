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
            <router-link :to="item.link" class="nav-link" >{{ item.name }}</router-link>
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


export default {
  name: 'Nav-bar',
  data(){
    return{
      isDropdownOpen: false, // Track the dropdown state
      languages: ['EN', '中文'], // Replace with your desired language options
      selectedLanguage: 'EN' ,  // Set the default selected language
      navitems:[
        { id: 1, name: "Home Page", link:"/" },
        { id: 2, name: "Blogs", link:"/blogs" },
        { id: 3, name: "Publications" , link:"/publications"},
        { id: 4, name: "My Resource", link:"/resources"},
        { id: 5, name: "About Me", link:"aboutme"},
        {id: 6, name: "Gallery", link:"gallery"}
      ],
    };
  },
  methods: {
    selectLanguage(language) {
      if(language === "EN"){
        this.selectedLanguage = "EN";
      }
      else{
        this.selectedLanguage = "中文";
      }
      //send this language selection to whole project
      this.$emit("SelectLan",this.selectedLanguage);

      this.isDropdownOpen = false;
      let navitems1=[
        { id: 1, name: "Home Page", link:"/" },
        { id: 2, name: "Blogs", link:"/blogs" },
        { id: 3, name: "Publications" , link:"/publications"},
        { id: 4, name: "My Resource", link:"/resources"},
        { id: 5, name: "About Me", link:"aboutme"},
        {id: 6, name: "Gallery", link:"gallery"}
      ];
      let   navitems2=[
        { id: 1, name: "主页", link:"/" },
        { id: 2, name: "博客", link:"/blogs" },
        { id: 3, name: "出版" , link:"/publications"},
        { id: 4, name: "我的资源", link:"/resources"},
        { id: 5, name: "关于我", link:"aboutme"},
        {id: 6, name: "我的瞬间", link:"gallery"}
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
