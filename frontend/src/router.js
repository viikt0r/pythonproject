import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './views/Dashboard.vue'
import Deals from './views/Deals'
import Brands from './views/Brands'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/Deals',
      name: 'deals',
      component: Deals
    },
    {
      path: '/Brands',
      name: 'brands',
      component: Brands
    }  
  ]
})
