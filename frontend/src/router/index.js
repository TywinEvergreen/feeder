import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Feed',
        component: () => import('../views/Feed.vue')
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('../views/Login.vue')
    },
    {
        path: '/register',
        name: 'Register',
        component: () => import('../views/Register.vue')
    },
    {
        path: '/profile',
        name: 'Profile',
        component: () => import('../views/Profile.vue')
    },
    {
        path: '/add-artist',
        name: 'AddArtist',
        component: () => import('../views/AddArtist.vue')
    },
    {
        path: '/add-channel',
        name: 'AddChannel',
        component: () => import('../views/AddChannel.vue')
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    const auth_pages = ['Login', 'Register'];
    if (!store.getters.auth_token_in_cookies && !auth_pages.includes(to.name)) {
        next({name: 'Login'})
    } else {
        next()
    }
})

export default router
