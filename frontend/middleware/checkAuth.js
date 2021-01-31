export default function ({ store, route, app }) {
    const auth = store.state.user.isAuthenticated;
    const auth_pages = ['user-login', 'user-register'];
    if (!auth && !auth_pages.includes(route.name)) {
        return app.router.push('user/login')
    }
}
