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
        component:HomePage,
        props: route => ({ lang: route.query.lang })
    },
    {
        path: "/aboutme",
        name: "aboutme",
        component: AboutMe,
        props: route => ({ lang: route.query.lang })
    },
    {
        path: "/blogs",
        name: "blogs",
        component: Blogs,
        props: route => ({ lang: route.query.lang })
    },
    {
        path: "/gallery",
        name: "gallery",
        component: Gallery,
        props: route => ({ lang: route.query.lang })
    },
    {
        path: "/resources",
        name: "resources",
        component: Resources,
        props: route => ({ lang: route.query.lang })
    },
    {
        path: "/publications",
        name: "publication",
        component: Publications,
        props: route => ({ query: route.query.lang })
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router;