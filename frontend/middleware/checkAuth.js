export default function ({ store, route, redirect }) {
    // Разобраться с проблемой, когда пользователя редиректит
    // даже если он аутентифицирова
    const auth = store.state.user.isAuthenticated;
    const auth_pages = ['user-login', 'user-register'];
    if (!auth && !auth_pages.includes(route.name)) {
        return redirect('/user/login')
    }
}
