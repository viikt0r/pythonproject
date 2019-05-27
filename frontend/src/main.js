import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import VueResource from 'vue-resource'
import router from './router'
import Axios from 'axios'
import store from './store'


Vue.use(Vuetify)
Vue.use(VueResource)

Vue.config.productionTip = false

//const axiosApi = Axios.create({
//  baseURL: (process.env.VUE_APP_BASE_URL !== undefined) ? process.env.VUE_APP_BASE_URL : '//trackerapp.local/'
//})


const token = localStorage.getItem('token')
if (token) {
  Axios.defaults.headers.common['Authorization'] = token
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

