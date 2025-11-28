import { createRouter, createWebHistory } from 'vue-router'
import Landing from '../views/Landing.vue'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Agendamentos from '../views/Agendamentos.vue'
import ClienteDashboard from '../views/ClienteDashboard.vue'
import Configuracoes from '../views/Configuracoes.vue' // Importar Configuracoes.vue

const routes = [
  { path: '/', name: 'Landing', component: Landing },
  { path: '/app', name: 'Dashboard', component: Home, meta: { requiresAuth: true, requiresAdmin: true } },
  { path: '/app/agendamentos', name: 'Agendamentos', component: Agendamentos, meta: { requiresAuth: true, requiresAdmin: true } },
  { path: '/app/configuracoes', name: 'Configuracoes', component: Configuracoes, meta: { requiresAuth: true, requiresAdmin: true } }, // Nova rota
  { path: '/cliente', name: 'Cliente', component: ClienteDashboard, meta: { requiresAuth: true } },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access')
  const isStaff = localStorage.getItem('is_staff') === 'true' // localStorage armazena strings

  if (to.meta.requiresAuth && !token) {
    return next({ name: 'Login' })
  }

  if ((to.name === 'Login' || to.name === 'Register') && token) {
    if (isStaff) {
      return next({ name: 'Dashboard' }) // Admin
    } else {
      return next({ name: 'Cliente' }) // Cliente
    }
  }

  // Proteção das rotas de admin
  if (to.meta.requiresAdmin && !isStaff) {
    return next({ name: 'Cliente' })
  }

  next()
})

export default router
