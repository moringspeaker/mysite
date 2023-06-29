import { createStore } from 'vuex';

export default createStore({
    state: {
        lang: 'EN', // The initial state
        cn: null
    },
    mutations: {
        // Mutation to set language
        setLanguage(state, lang) {
            state.lang = lang;
        },
        // You can add more mutations here as needed
    },
    actions: {
        // Actions can be used to commit mutations and can contain asynchronous operations
    },
    getters: {
        // Getters can be used to compute derived state based on store state
    }
});
