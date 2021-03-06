import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './views/Dashboard.vue'
import Deals from './views/Deals'
import Deal from './views/Deal'
import Brands from './views/Brands'
import Brand from './views/Brand'
import Login from './components/Login'
import Register from './components/Register'
import Secure from './components/Secure'
import store from './store.js'


Vue.use(Router)

let router = new Router({
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
      path: '/Deals/:id',
      name: 'deal',
      component: Deal
    },
    {
      path: '/Brands',
      name: 'brands',
      component: Brands
    },
    {
      path: '/Brands/:id',
      name: 'brand',
      component: Brand,
    },
    {
      path: '/Login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/secure',
      name: 'secure',
      component: Secure,
      meta: {
        requiresAuth: true
      }
    },

  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login')
  } else {
    next()
  }
})

export default router