import { createStore } from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'  // <-- Import the plugin

export default createStore({
    plugins: [createPersistedState()], // <-- Use the plugin
    state: {
        lang: 'EN',
        user: null,
        token: localStorage.getItem('token') || '',
        status: '',
        cn: null,
        isLoggedIn: false,
        currentHeaderIndex: null,
    },
    mutations: {
        setCurrentHeaderIndex(state, currentHeaderIndex) {
            state.currentHeaderIndex = currentHeaderIndex;
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
        },
        auth_error(state) {
            state.status = 'error'
        },
        logout(state) {
            state.status = ''
            state.token = ''
        },
        set_isLoggedIn(state, status) {
            state.isLoggedIn = status
        },
    },
    actions: {
        async login({ commit }, user) {
            commit('auth_request')
            try {
                let response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}api/superuser_login/`, user)
                const token = response.data.token
                console.log(token);
                localStorage.setItem('token', token)
                axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
                commit('auth_success', token)
                commit('set_isLoggedIn', true)
            } catch (error) {
                commit('auth_error')
                localStorage.removeItem('token')
                throw error
            }
        },
        logout({ commit }) {
            return new Promise((resolve) => {
                commit('logout')
                localStorage.removeItem('token')
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
