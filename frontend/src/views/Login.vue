<template>
  <div class="auth">
    <h2>{{ $t('login.title') }}</h2>
    <form @submit.prevent="submit">
      <div>
        <label>{{ $t('login.username') }}</label>
        <input v-model="username" />
      </div>
      <div>
        <label>{{ $t('login.password') }}</label>
        <input type="password" v-model="password" />
      </div>
      <button type="submit">{{ $t('login.submit') }}</button>
    </form>
    <p>
      <router-link to="/register">{{ $t('login.noAccount') }}</router-link>
    </p>
  </div>
</template>

<script>
import { login } from '../composables/useAuth'

export default {
  name: 'Login',
  data() {
    return { username: '', password: '' }
  },
  methods: {
    async submit() {
      try {
        await login(this.username, this.password)
        this.$router.push({ name: 'Dashboard' })
      } catch (err) {
        alert('Erro ao efetuar login')
      }
    }
  }
}
</script>

<style scoped>
.auth { max-width: 420px; margin: 2rem auto; padding: 1rem; }
</style>
