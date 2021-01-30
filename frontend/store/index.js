import Vuex from 'vuex';

import conf from './modules/conf'
import user from './modules/user'
import utils from './modules/utils'

// Можно сделать как в https://github.com/xuqiang521/nuxt-ssr-demo/blob/dev/store/index.js

export default () => new Vuex.Store({
    modules: {
        conf,
        user,
        utils
    }
})