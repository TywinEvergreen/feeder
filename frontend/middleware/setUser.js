export default async function ({store}) {
    if (!!localStorage.getItem('auth._token.local')) {
        await store.dispatch('user/set_authorization_header')
        await store.dispatch('user/set_user')
    }
}
