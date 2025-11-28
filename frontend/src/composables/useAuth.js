import axios from 'axios'
import api from '../services/api'

const baseRefreshUrl = api.defaults.baseURL + '/auth/token/refresh/'

export async function login(username, password) {
  const r = await api.post('/auth/token/', { username, password })
  if (r && r.data) {
    localStorage.setItem('access', r.data.access)
    localStorage.setItem('refresh', r.data.refresh)
    api.defaults.headers.common['Authorization'] = 'Bearer ' + r.data.access
  }
  return r.data
}

export async function register(payload) {
  const r = await api.post('/auth/register/', payload)
  return r.data
}

export async function logout() {
  const refresh = localStorage.getItem('refresh')
  try {
    if (refresh) {
      // use bare axios to avoid interceptors
      // Correção: construir a URL de logout corretamente
      await axios.post(api.defaults.baseURL + '/auth/logout/', { refresh })
    }
  } catch (e) {
    // ignore
  }
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
}

export async function refreshToken() {
  const refresh = localStorage.getItem('refresh')
  if (!refresh) throw new Error('No refresh token')
  const r = await axios.post(baseRefreshUrl, { refresh })
  if (r && r.data) {
    localStorage.setItem('access', r.data.access)
    api.defaults.headers.common['Authorization'] = 'Bearer ' + r.data.access
  }
  return r.data
}

export function isAuthenticated() {
  return !!localStorage.getItem('access')
}

export default {
  login,
  register,
  logout,
  refreshToken,
  isAuthenticated
}
