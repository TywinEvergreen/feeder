import Axios from "axios";
import Cookies from 'js-cookie';

export const state = () => ({
    user: null,
    authenticated: false
});

export const getters = () => ({
    auth_token_in_cookies: () => {
        return !!Cookies.get('auth_token');
    }
});

export const mutations = () => ({
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
        Axios.defaults.headers.common['Authorization'] = 'Token ' + payload;
    },
});

export const actions = () => ({
    set_user: async ({commit}) => {
        await Axios.get('auth/users/me/')
            .then(response => {
                commit('user', response.data);
                commit('authenticated', true)
            })
            .catch(error => {
                if (error.response.data.detail === 'Недопустимый токен.') {
                    delete Axios.defaults.headers.common['Authorization'];
                }
                commit('authenticated', false);
            });
        commit('show_authentication_menu', true);
    },
    set_authorization_header: async ({commit}) => {
        let auth_token = Cookies.get('auth_token');
        commit('authorization_header', auth_token);
    },
});
