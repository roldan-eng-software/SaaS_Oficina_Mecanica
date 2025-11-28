import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  headers: { 'Content-Type': 'application/json' },
  withCredentials: true
})

// Attach Authorization header when access token exists
api.interceptors.request.use(config => {
  if (config.skipAuth) return config
  const token = localStorage.getItem('access')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

// Automatic refresh logic
let isRefreshing = false
let failedQueue = []

const processQueue = (error, token = null) => {
  failedQueue.forEach(prom => {
    if (error) {
      prom.reject(error)
    } else {
      prom.resolve(token)
    }
  })
  failedQueue = []
}

api.interceptors.response.use(
  response => response,
  error => {
    console.log("Erro no interceptor de resposta da API:", error.response); // Adicionar este log
    const originalRequest = error.config
    if (!originalRequest) return Promise.reject(error)

    const status = error.response ? error.response.status : null

    if (status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      const refresh = localStorage.getItem('refresh')

      if (!refresh) {
        // sem refresh, forçar logout
        localStorage.removeItem('access')
        localStorage.removeItem('refresh')
        window.location.href = '/login'
        return Promise.reject(error)
      }

      if (isRefreshing) {
        return new Promise(function (resolve, reject) {
          failedQueue.push({ resolve, reject })
        })
          .then(token => {
            originalRequest.headers['Authorization'] = 'Bearer ' + token
            return api(originalRequest)
          })
          .catch(err => Promise.reject(err))
      }

      isRefreshing = true

      return new Promise(function (resolve, reject) {
        // usar axios sem interceptors para evitar loop; chamar endpoint /auth/refresh/ que lê cookie HttpOnly
        axios
          .post(api.defaults.baseURL + '/auth/refresh/', null, { withCredentials: true })
          .then(({ data }) => {
            localStorage.setItem('access', data.access)
            api.defaults.headers.common['Authorization'] = 'Bearer ' + data.access
            processQueue(null, data.access)
            originalRequest.headers['Authorization'] = 'Bearer ' + data.access
            resolve(api(originalRequest))
          })
          .catch(err => {
            processQueue(err, null)
            localStorage.removeItem('access')
            localStorage.removeItem('refresh')
            window.location.href = '/login'
            reject(err)
          })
          .finally(() => {
            isRefreshing = false
          })
      })
    }

    return Promise.reject(error)
  }
)

export default api
