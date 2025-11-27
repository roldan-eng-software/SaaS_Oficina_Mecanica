import { createRouter, createWebHistory } from 'vue-router'
import Landing from '../views/Landing.vue'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

const routes = [
  { path: '/', name: 'Landing', component: Landing },
  { path: '/app', name: 'Dashboard', component: Home, meta: { requiresAuth: true } },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access')
  if (to.meta.requiresAuth && !token) return next({ name: 'Login' })
  if ((to.name === 'Login' || to.name === 'Register') && token) return next({ name: 'Dashboard' })
  next()
})

export default router
