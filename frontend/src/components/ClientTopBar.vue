<template>
  <header class="bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 px-6 py-4">
    <div class="flex items-center justify-between">
      <!-- Logo -->
      <div class="flex items-center gap-3">
        <span class="material-symbols-outlined text-3xl text-primary">directions_car</span>
        <h1 class="text-xl font-bold text-text-light dark:text-text-dark">AutoExpert</h1>
      </div>

      <!-- User Menu -->
      <div class="flex items-center gap-4">
        <div class="relative">
          <button
            @click="showDropdown = !showDropdown"
            class="flex items-center gap-3 px-3 py-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
          >
            <div class="w-8 h-8 bg-primary rounded-full flex items-center justify-center">
              <span class="material-symbols-outlined text-white text-sm">person</span>
            </div>
            <div class="text-left hidden sm:block">
              <p class="text-sm font-medium text-text-light dark:text-text-dark">Cliente</p>
            </div>
            <span class="material-symbols-outlined text-text-muted-light dark:text-text-muted-dark">expand_more</span>
          </button>

          <!-- Dropdown Menu -->
          <div
            v-if="showDropdown"
            class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 py-2 z-50"
          >
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
  name: 'ClientTopBar',
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
    document.addEventListener('click', (e) => {
      if (!this.$el.contains(e.target)) {
        this.showDropdown = false
      }
    })
  }
}
</script>
