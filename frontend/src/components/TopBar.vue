<template>
  <header class="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 px-6 py-4">
    <div class="flex items-center justify-between">
      <!-- Page Title -->
      <div>
        <h2 class="text-2xl font-bold text-text-light dark:text-text-dark">{{ title }}</h2>
        <p v-if="subtitle" class="text-sm text-text-muted-light dark:text-text-muted-dark mt-1">{{ subtitle }}</p>
      </div>

      <!-- User Menu -->
      <div class="flex items-center gap-4">
        <!-- Notifications (placeholder) -->
        <button class="relative p-2 text-text-muted-light dark:text-text-muted-dark hover:text-primary transition-colors">
          <span class="material-symbols-outlined">notifications</span>
          <span class="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
        </button>

        <!-- User Dropdown -->
        <div class="relative">
          <button
            @click="showDropdown = !showDropdown"
            class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
          >
            <div class="w-8 h-8 bg-primary rounded-full flex items-center justify-center">
              <span class="material-symbols-outlined text-white text-sm">person</span>
            </div>
            <div class="text-left hidden sm:block">
              <p class="text-sm font-medium text-text-light dark:text-text-dark">Admin</p>
              <p class="text-xs text-text-muted-light dark:text-text-muted-dark">admin@autoexpert.com</p>
            </div>
            <span class="material-symbols-outlined text-text-muted-light dark:text-text-muted-dark">expand_more</span>
          </button>

          <!-- Dropdown Menu -->
          <div
            v-if="showDropdown"
            class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 py-2 z-50"
          >
            <router-link
              to="/app/perfil"
              class="flex items-center gap-3 px-4 py-2 text-sm text-text-light dark:text-text-dark hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
              @click="showDropdown = false"
            >
              <span class="material-symbols-outlined text-lg">person</span>
              Meu Perfil
            </router-link>
            <router-link
              to="/app/configuracoes"
              class="flex items-center gap-3 px-4 py-2 text-sm text-text-light dark:text-text-dark hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
              @click="showDropdown = false"
            >
              <span class="material-symbols-outlined text-lg">settings</span>
              Configurações
            </router-link>
            <hr class="my-2 border-gray-200 dark:border-gray-700" />
            <button
              @click="handleLogout"
              class="flex items-center gap-3 px-4 py-2 text-sm text-red-600 dark:text-red-400 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors w-full text-left"
            >
              <span class="material-symbols-outlined text-lg">logout</span>
              Sair
            </button>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import { logout } from '../composables/useAuth'

export default {
  name: 'TopBar',
  props: {
    title: {
      type: String,
      default: 'Dashboard'
    },
    subtitle: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      showDropdown: false
    }
  },
  methods: {
    async handleLogout() {
      try {
        await logout()
      } catch (e) {
        // ignore
      }
      this.$router.push({ name: 'Login' })
    }
  },
  mounted() {
    // Close dropdown when clicking outside
    document.addEventListener('click', (e) => {
      if (!this.$el.contains(e.target)) {
        this.showDropdown = false
      }
    })
  }
}
</script>
