<template>
  <div class="home">
    <h1>{{ $t('home.title') }}</h1>
    <button @click="logout">{{ $t('home.logout') }}</button>
    <ul>
      <li v-for="s in servicos" :key="s.id">{{ s.veiculo }} — {{ s.cliente }} — {{ s.concluido ? 'Concluído' : 'Pendente' }}</li>
    </ul>
  </div>
</template>

<script>
import api from '../services/api'
import { logout as authLogout } from '../composables/useAuth'

export default {
  name: 'Home',
  data() {
    return { servicos: [] }
  },
  async created() {
    try {
      const r = await api.get('/servicos/')
      this.servicos = r.data
    } catch (err) {
      console.error(err)
    }
  },
  methods: {
    async logout() {
      try {
        await authLogout()
      } catch (e) {
        // ignore
      }
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style scoped>
.home { padding: 1rem; }
</style>
