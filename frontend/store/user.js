import Cookies from 'js-cookie';


export const state = () => ({
    user: null,
    isAuthenticated: false
})

export const getters = {
    auth_token_in_cookies: () => !!Cookies.get('auth_token'),
}

export const mutations = {
    user(state, payload) {
        state.user = payload
    },
    isAuthenticated(state, payload) {
        state.isAuthenticated = payload
    },
}

export const actions = {
    async set_user({ commit }) {
        await this.$axios.$get('auth/users/me/')
            .then(response => {
                commit('user', response);
                commit('isAuthenticated', true)
            })
            .catch(error => {
                if (error.response.data.detail === 'Недопустимый токен.') {
                    delete this.$axios.defaults.headers.common['Authorization'];
                }
                commit('isAuthenticated', false);
            });
    },
    async set_authorization_header() {
        let auth_token = Cookies.get('auth_token');
        this.$axios.defaults.headers.common['Authorization'] = 'Token ' + auth_token;
    },
}
