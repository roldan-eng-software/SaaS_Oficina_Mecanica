<template>
  <div class="flex min-h-screen items-center justify-center bg-background-light dark:bg-background-dark px-4 py-12 sm:px-6 lg:px-8">
    <div class="w-full max-w-md space-y-8 bg-white dark:bg-gray-900 p-8 rounded-xl shadow-lg border border-gray-200 dark:border-gray-800">
      <div class="text-center">
        <span class="material-symbols-outlined text-5xl text-primary mb-2">person_add</span>
        <h2 class="mt-2 text-3xl font-bold tracking-tight text-text-light dark:text-text-dark">
          Crie sua conta
        </h2>
        <p class="mt-2 text-sm text-text-muted-light dark:text-text-muted-dark">
          Junte-se a nós para agendar serviços com facilidade
        </p>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="submit">
        <div class="-space-y-px rounded-md shadow-sm">
          <div class="grid grid-cols-2 gap-4 mb-4">
            <div class="relative">
              <label for="first_name" class="sr-only">Nome</label>
              <input
                id="first_name"
                name="first_name"
                type="text"
                required
                v-model="first_name"
                class="relative block w-full rounded-lg border-0 py-3 px-4 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6 dark:bg-gray-800 dark:text-white dark:ring-gray-700 dark:placeholder:text-gray-500"
                placeholder="Nome"
              />
            </div>
            <div class="relative">
              <label for="last_name" class="sr-only">Sobrenome</label>
              <input
                id="last_name"
                name="last_name"
                type="text"
                required
                v-model="last_name"
                class="relative block w-full rounded-lg border-0 py-3 px-4 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6 dark:bg-gray-800 dark:text-white dark:ring-gray-700 dark:placeholder:text-gray-500"
                placeholder="Sobrenome"
              />
            </div>
          </div>

          <div class="relative mb-4">
            <label for="username" class="sr-only">{{ $t('register.username') }}</label>
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
              :placeholder="$t('register.username')"
            />
          </div>

          <div class="relative mb-4">
            <label for="email" class="sr-only">{{ $t('register.email') }}</label>
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <span class="material-symbols-outlined text-gray-400">email</span>
            </div>
            <input
              id="email"
              name="email"
              type="email"
              required
              v-model="email"
              class="relative block w-full rounded-lg border-0 py-3 pl-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:z-10 focus:ring-2 focus:ring-inset focus:ring-primary sm:text-sm sm:leading-6 dark:bg-gray-800 dark:text-white dark:ring-gray-700 dark:placeholder:text-gray-500"
              :placeholder="$t('register.email')"
            />
          </div>

          <div class="relative">
            <label for="password" class="sr-only">{{ $t('register.password') }}</label>
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
              :placeholder="$t('register.password')"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            :disabled="loading"
            class="group relative flex w-full justify-center rounded-lg bg-primary px-3 py-3 text-sm font-semibold text-white hover:opacity-90 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:opacity-70 disabled:cursor-not-allowed transition-all"
          >
            <span class="absolute inset-y-0 left-0 flex items-center pl-3" v-if="!loading">
              <span class="material-symbols-outlined text-white/70 group-hover:text-white">person_add</span>
            </span>
            <span v-if="loading" class="flex items-center gap-2">
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Criando conta...
            </span>
            <span v-else>{{ $t('register.submit') }}</span>
          </button>
        </div>

        <div v-if="error" class="rounded-md bg-red-50 dark:bg-red-900/30 p-4">
          <div class="flex">
            <div class="flex-shrink-0">
              <span class="material-symbols-outlined text-red-400">error</span>
            </div>
            <div class="ml-3">
              <h3 class="text-sm font-medium text-red-800 dark:text-red-200">Erro no registro</h3>
              <div class="mt-2 text-sm text-red-700 dark:text-red-300">
                <p>{{ error }}</p>
              </div>
            </div>
          </div>
        </div>
      </form>
      
      <div class="text-center mt-4">
        <p class="text-sm text-text-muted-light dark:text-text-muted-dark">
          Já tem uma conta?
          <router-link to="/login" class="font-medium text-primary hover:text-primary/80 transition-colors">
            {{ $t('register.haveAccount') }}
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { register } from '../composables/useAuth'

export default {
  name: 'Register',
  data() {
    return {
      first_name: '',
      last_name: '',
      username: '',
      email: '',
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
        await register({
          username: this.username,
          email: this.email,
          password: this.password,
          first_name: this.first_name,
          last_name: this.last_name
        })
        // após registro, redireciona para login
        this.$router.push({ name: 'Login' })
      } catch (err) {
        console.error(err)
        this.error = 'Erro ao criar conta. Verifique os dados e tente novamente.'
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
