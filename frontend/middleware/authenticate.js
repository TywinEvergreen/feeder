export default function ({ store }) {
    store.dispatch('user/set_authorization_header');
    store.dispatch('user/set_user');
}
