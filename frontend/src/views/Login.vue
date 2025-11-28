<template>
  <div class="flex min-h-screen items-center justify-center bg-background-light dark:bg-background-dark px-4 py-12 sm:px-6 lg:px-8">
    <div class="w-full max-w-md space-y-8 bg-white dark:bg-gray-900 p-8 rounded-xl shadow-lg border border-gray-200 dark:border-gray-800">
      <div class="text-center">
        <span class="material-symbols-outlined text-5xl text-primary mb-2">directions_car</span>
        <h2 class="mt-2 text-3xl font-bold tracking-tight text-text-light dark:text-text-dark">
          Bem-vindo de volta
        </h2>
        <p class="mt-2 text-sm text-text-muted-light dark:text-text-muted-dark">
          Acesse sua conta para gerenciar seus agendamentos
        </p>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="submit">
        <div class="-space-y-px rounded-md shadow-sm">
          <div class="relative mb-4">
            <label for="username" class="sr-only">{{ $t('login.username') }}</label>
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <span class="material-symbols-outlined text-gray-400">person</span>
            </div>
            <input
              id="username"
              name="username"
              type="text"
              required
              v-model="username"
              class="relative block w-full rounded-lg border-0 py-3 pl-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6 dark:bg-gray-800 dark:text-white dark:ring-gray-700 dark:placeholder:text-gray-500"
              :placeholder="$t('login.username')"
            />
          </div>
          <div class="relative">
            <label for="password" class="sr-only">{{ $t('login.password') }}</label>
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <span class="material-symbols-outlined text-gray-400">lock</span>
            </div>
            <input
              id="password"
              name="password"
              type="password"
              required
              v-model="password"
              class="relative block w-full rounded-lg border-0 py-3 pl-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6 dark:bg-gray-800 dark:text-white dark:ring-gray-700 dark:placeholder:text-gray-500"
              :placeholder="$t('login.password')"
            />
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember-me"
              name="remember-me"
              type="checkbox"
              class="h-4 w-4 rounded border-gray-300 text-primary focus:ring-primary dark:border-gray-600 dark:bg-gray-700"
            />
            <label for="remember-me" class="ml-2 block text-sm text-text-light dark:text-text-dark">
              Lembrar de mim
            </label>
          </div>

          <div class="text-sm">
            <a href="#" class="font-medium text-primary hover:text-primary/80">
              Esqueceu a senha?
            </a>
          </div>
        </div>

        <div>
          <button
            type="submit"
            :disabled="loading"
            class="group relative flex w-full justify-center rounded-lg bg-primary px-3 py-3 text-sm font-semibold text-white hover:opacity-90 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:opacity-70 disabled:cursor-not-allowed transition-all"
          >
            <span class="absolute inset-y-0 left-0 flex items-center pl-3" v-if="!loading">
              <span class="material-symbols-outlined text-white/70 group-hover:text-white">login</span>
            </span>
            <span v-if="loading" class="flex items-center gap-2">
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Entrando...
            </span>
            <span v-else>{{ $t('login.submit') }}</span>
          </button>
        </div>

        <div v-if="error" class="rounded-md bg-red-50 dark:bg-red-900/30 p-4">
          <div class="flex">
            <div class="flex-shrink-0">
              <span class="material-symbols-outlined text-red-400">error</span>
            </div>
            <div class="ml-3">
              <h3 class="text-sm font-medium text-red-800 dark:text-red-200">Erro no login</h3>
              <div class="mt-2 text-sm text-red-700 dark:text-red-300">
                <p>{{ error }}</p>
              </div>
            </div>
          </div>
        </div>
      </form>
      
      <div class="text-center mt-4">
        <p class="text-sm text-text-muted-light dark:text-text-muted-dark">
          Não tem uma conta?
          <router-link to="/register" class="font-medium text-primary hover:text-primary/80 transition-colors">
            {{ $t('login.noAccount') }}
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { login } from '../composables/useAuth'
import api from '../services/api' // Importar api

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      error: null
    }
  },
  methods: {
    async submit() {
      this.loading = true
      this.error = null
      try {
        await login(this.username, this.password)
        
        // Após login, buscar dados do usuário
        const { data: userData } = await api.get('/users/me/')
        
        // Armazenar is_staff no localStorage
        localStorage.setItem('is_staff', userData.is_staff)
        
        // Redirecionar para a Dashboard, e o router.beforeEach cuidará do redirecionamento final com base em is_staff
        this.$router.push({ name: 'Dashboard' })
        
      } catch (err) {
        console.error(err)
        this.error = 'Usuário ou senha incorretos. Por favor, tente novamente.'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
/* Scoped styles removed in favor of Tailwind classes */
</style>
