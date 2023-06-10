import {createRouter, createWebHashHistory} from "vue-router";

import AboutMe from "@/views/AboutMe.vue";
import Blogs from "@/views/Blogs.vue";
import Gallery from "@/views/Gallery.vue";
import Publications from "@/views/Publications.vue";
import Resources from "@/views/Resources.vue";
import HomePage from "@/views/HomePage.vue";


const routes = [
    {
        path: "/",
        name: "homepage",
        component:HomePage
    },
    {
        path: "/aboutme",
        name: "aboutme",
        component: AboutMe
    },
    {
        path: "/blogs",
        name: "blogs",
        component: Blogs
    },
    {
        path: "/gallery",
        name: "gallery",
        component: Gallery
    },
    {
        path: "/resources",
        name: "resources",
        component: Resources
    },
    {
        path: "/publications",
        name: "publication",
        component: Publications
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router;