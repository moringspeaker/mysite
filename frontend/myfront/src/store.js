import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
    state: {
        lang: 'EN',
        user: null, // stores the logged in user data
        token: localStorage.getItem('token') || '',
        status: '', // stores authentication status
        cn: null,
        isLoggedIn: false,
    },
    mutations: {
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
            state.status = 'error'  // further can have a fake logged in page and allow user to try to write blogs but discard whatever they write
        },
        logout(state) {
            state.status = ''
            state.token = ''
        },
        set_isLoggedIn(state, status) { // <== ADD THIS MUTATION
            state.isLoggedIn = status
        },
    },
    actions: {
        async login({ commit }, user) {
            commit('auth_request')
            try {
                let response = await axios.post(`${process.env.VUE_APP_BACKEND_URL}user/api/superuser_login/`, user)
                const token = response.data.token
                console.log(token);
                localStorage.setItem('token', token)
                axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
                commit('auth_success', token) // auth_success mutation updates the state with the token
                commit('set_isLoggedIn', true) // <== ADD THIS LINE
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
        isLoggedIn: state => state.isLoggedIn,
        authStatus: state => state.status,
    }
});
