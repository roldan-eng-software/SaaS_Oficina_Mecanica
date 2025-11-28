<template>
  <aside class="w-64 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 flex flex-col h-screen">
    <!-- Logo -->
    <div class="p-6 border-b border-gray-200 dark:border-gray-800">
      <div class="flex items-center gap-3">
        <span class="material-symbols-outlined text-3xl text-primary">directions_car</span>
        <h1 class="text-xl font-bold text-text-light dark:text-text-dark">AutoExpert</h1>
      </div>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 p-4 space-y-2">
      <router-link
        to="/app"
        class="flex items-center gap-3 px-4 py-3 rounded-lg text-text-light dark:text-text-dark hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
        active-class="bg-primary/10 text-primary hover:bg-primary/20"
      >
        <span class="material-symbols-outlined">dashboard</span>
        <span class="font-medium">Dashboard</span>
      </router-link>

      <router-link
        to="/app/agendamentos"
        class="flex items-center gap-3 px-4 py-3 rounded-lg text-text-light dark:text-text-dark hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
        active-class="bg-primary/10 text-primary hover:bg-primary/20"
      >
        <span class="material-symbols-outlined">event</span>
        <span class="font-medium">Agendamentos</span>
      </router-link>

      <router-link
        to="/cliente"
        class="flex items-center gap-3 px-4 py-3 rounded-lg text-text-light dark:text-text-dark hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
        active-class="bg-primary/10 text-primary hover:bg-primary/20"
      >
        <span class="material-symbols-outlined">people</span>
        <span class="font-medium">Clientes</span>
      </router-link>

      <router-link
        to="/app/configuracoes"
        class="flex items-center gap-3 px-4 py-3 rounded-lg text-text-light dark:text-text-dark hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
        active-class="bg-primary/10 text-primary hover:bg-primary/20"
      >
        <span class="material-symbols-outlined">settings</span>
        <span class="font-medium">Configurações</span>
      </router-link>
    </nav>

    <!-- Footer -->
    <div class="p-4 border-t border-gray-200 dark:border-gray-800">
      <p class="text-xs text-text-muted-light dark:text-text-muted-dark text-center">
        © 2024 AutoExpert
      </p>
    </div>
  </aside>
</template>

<script>
export default {
  name: 'Sidebar'
}
</script>
