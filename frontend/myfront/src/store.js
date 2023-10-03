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
        search:'',
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
        ],
    },
    mutations: {
        setCurrentHeaderIndex(state, currentHeaderIndex) {
            state.currentHeaderIndex = currentHeaderIndex;
        },
         setSearch(state, keyword) {
        state.search = keyword;
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
            state.isLoggedIn = true
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
                let response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}api/user/login/`, user)
                const token = response.data.token;
                const username = response.data.username;
                axios.defaults.headers.common['Authorization'] = 'Token ' + token;
                commit('auth_success', { token, user: username })
            } catch (error) {
                commit('auth_error')
                throw error
            }
        },
        updateSearch({ commit }, keyword) {
        commit('setSearch', keyword);
        },
        async logout({ commit }) {
            await axios.get(`${process.env.VUE_APP_BACKEND_URL}api/user/logout/`);
            commit('logout');
            delete axios.defaults.headers.common['Authorization'];
            return Promise.resolve();
        },
    },
    getters: {
        currentLanguage: state => state.lang,
        isLoggedIn: state => state.isLoggedIn,
        authStatus: state => state.status,
    }
});
