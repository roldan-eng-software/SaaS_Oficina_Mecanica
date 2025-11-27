<template>
  <div class="auth">
    <h2>{{ $t('register.title') }}</h2>
    <form @submit.prevent="submit">
      <div>
        <label>{{ $t('register.username') }}</label>
        <input v-model="username" />
      </div>
      <div>
        <label>{{ $t('register.email') }}</label>
        <input v-model="email" />
      </div>
      <div>
        <label>{{ $t('register.password') }}</label>
        <input type="password" v-model="password" />
      </div>
      <button type="submit">{{ $t('register.submit') }}</button>
    </form>
    <p>
      <router-link to="/login">{{ $t('register.haveAccount') }}</router-link>
    </p>
  </div>
</template>

<script>
import { register } from '../composables/useAuth'

export default {
  name: 'Register',
  data() {
    return { username: '', email: '', password: '' }
  },
  methods: {
    async submit() {
      try {
        await register({ username: this.username, email: this.email, password: this.password })
        // após registro, redireciona para login
        this.$router.push({ name: 'Login' })
      } catch (err) {
        alert('Erro ao registrar usuário')
      }
    }
  }
}
</script>

<style scoped>
.auth { max-width: 420px; margin: 2rem auto; padding: 1rem; }
</style>
