import Cookies from 'js-cookie';


export const state = () => ({
    user: null,
    isAuthenticated: false
})

export const getters = {
    auth_token_in_cookies: () => {
        return !!Cookies.get('auth_token')
    },
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
                commit('isAuthenticated', true);
            })
            .catch(error => {
                console.log(error);
                if (error.response.detail === 'Недопустимый токен.') {
                    delete this.$axios.defaults.headers.common['Authorization'];
                }
                commit('isAuthenticated', false);
            });
    },
    async set_authorization_header() {
        let auth_token = await Cookies.get('auth._token.local');
        this.$axios.defaults.headers.common['Authorization'] = auth_token;
    },
}
