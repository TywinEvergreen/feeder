export default function ({ store, route, app }) {
    const auth = store.state.user.isAuthenticated;
    if (!auth && route.name != 'user-register') {
        app.router.push('user/login')
    }
}