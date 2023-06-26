import {createRouter, createWebHashHistory} from "vue-router";

import AboutMe from "@/views/MyInfo.vue";
import MyBlogs from "@/views/MyBlogs.vue";
import Gallery from "@/views/Gallery.vue";
import Publications from "@/views/Publications.vue";
import Resources from "@/views/Resources.vue";
import HomePage from "@/views/HomePage.vue";
import BlogPost from "@/views/BlogPost.vue";


const routes = [
    {
        path: "/",
        name: "homepage",
        component:HomePage,
        props: route => ({ lang: route.query.lang })
    },
    {
        path: "/myinfo",
        name: "myinfo",
        component: AboutMe,
        props: route => ({ lang: route.query.lang })
    },
    {
        path: "/blogs",
        name: "Myblogs",
        component: MyBlogs,
        props: route => ({ lang: route.query.lang })
    },
    {
        path: "/blogs/:id",
        name: "blogpost",
        component: BlogPost,
        props: route => ({ id: route.params.id, lang: route.query.lang })
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