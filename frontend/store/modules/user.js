import axios from 'axios';
import Cookies from 'js-cookie';

export default {
    state: () => ({
        user: null,
        isAuthenticated: false
    }),

    getters: {
        auth_token_in_cookies: () => !!Cookies.get('auth_token'),
    },

    mutations: {
        user: (payload) => {
            state.user = payload;
        },
        authenticated: (payload) => {
            state.authenticated = payload
        },
        show_authentication_menu: (payload) => {
            state.show_authentication_menu = payload
        },
        authorization_header: (context, payload) => {
            // axios.defaults.headers.common['Authorization'] = 'Token ' + payload;
        },
    },

    actions: {
        set_user: async (context) => {
            await axios.get('auth/users/me/')
                .then(response => {
                    commit('user', response.data);
                    commit('authenticated', true)
                })
                .catch(error => {
                    if (error.response.data.detail === 'Недопустимый токен.') {
                        // delete Axios.defaults.headers.common['Authorization'];
                    }
                    commit('authenticated', false);
                });
            commit('show_authentication_menu', true);
        },
        set_authorization_header: async ({commit}) => {
            let auth_token = Cookies.get('auth_token');
            commit('authorization_header', auth_token);
        },
    }
}
