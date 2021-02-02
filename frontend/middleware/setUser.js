export default function ({store}) {
    // Авторизация готова. Теперь нужно сделать так, чтобы
    // юзер всегда устанавливался корректно.
    if (!!localStorage.getItem('auth._token.local')) {
        store.dispatch('user/set_authorization_header')
        store.dispatch('user/set_user')
    }
}
