import { createStore } from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

export default createStore({
    plugins: [
        createPersistedState({
            paths: ['lang']  // Here we specify we only want to store 'lang' permanently
        }),
        createPersistedState({storage: window.sessionStorage})  // The rest of the state is stored in the session storage and will be cleared after the session ends
    ],
    state: {
        lang: 'EN',
        user: null,
        token: '',
        status: '',
        cn: null,
        isLoggedIn: false,
        currentHeaderIndex: null,
        navitems: [
            { id: 1, name: "Home Page", link:"/", icon: "bi bi-house-door" },
            { id: 2, name: "Blogs", link:"/blogs", icon: "bi bi-file-text" },
            { id: 3, name: "Publications" , link:"/publications", icon: "bi bi-journal-text" },
            { id: 4, name: "My Resource", link:"/resources", icon: "bi bi-folder" },
            { id: 5, name: "MyInfo", link:"/myinfo", icon: "bi bi-person-circle" },
            { id: 6, name: "Gallery", link:"/gallery", icon: "bi bi-images" },
            { id: 7, name: "Login", link:"/login", icon: "bi bi-box-arrow-in-right" }
        ],
    },
    mutations: {
        setCurrentHeaderIndex(state, currentHeaderIndex) {
            state.currentHeaderIndex = currentHeaderIndex;
        },
        setNavItems(state, items) {
            state.navitems = items;
        },
        setLanguage(state, lang) {
            state.lang = lang;
        },
        auth_request(state) {
            state.status = 'loading'
        },
        auth_success(state, { token, user }) {
            state.status = 'success'
            state.token = token
            state.user = user
            state.isLoggedIn = true // Set isLoggedIn true here
        },
        auth_error(state) {
            state.status = 'error'
        },
        logout(state) {
            state.status = ''
            state.token = ''
            state.isLoggedIn = false // Set isLoggedIn false here
        },
    },
    actions: {
        async login({ commit }, user) {
            commit('auth_request')
            try {
                let response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}api/superuser_login/`, user)
                const token = response.data.token
                axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
                commit('auth_success', { token, user: user }) // Pass user info here
            } catch (error) {
                commit('auth_error')
                throw error
            }
        },
        logout({ commit }) {
            return new Promise((resolve) => {
                commit('logout')
                delete axios.defaults.headers.common['Authorization']
                resolve()
            })
        },
    },
    getters: {
        currentLanguage: state => state.lang,
        isLoggedIn: state => state.isLoggedIn,
        authStatus: state => state.status,
    }
});
