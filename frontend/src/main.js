import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import Axios from 'axios'

Vue.config.productionTip = false;

if (process.env.NODE_ENV === 'production') {
  Axios.defaults.baseURL = 'http://127.0.0.1:8000/'
} else {
  Axios.defaults.baseURL = 'http://127.0.0.1:8000/'
}

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app');
