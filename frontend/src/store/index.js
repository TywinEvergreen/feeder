import Vue from 'vue'
import Vuex from 'vuex'
import conf from './modules/conf'
import user from './modules/user'
import utils from './modules/utils'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {},
    mutations: {},
    actions: {},
    modules: {
        conf,
        user,
        utils
    }
})