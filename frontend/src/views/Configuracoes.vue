<template>
  <div class="flex flex-col h-screen bg-background-light dark:bg-background-dark">
    <TopBar title="Configurações" subtitle="Gerencie as configurações da oficina" />
    <div class="flex flex-1">
      <Sidebar />
      <main class="flex-1 overflow-y-auto p-6">
        <div class="max-w-4xl mx-auto">
          <h1 class="text-3xl font-bold text-text-light dark:text-text-dark mb-6">Configurações da Oficina</h1>
          
          <!-- Seção de Gerenciamento de Tipos de Serviço -->
          <div class="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6 mb-8">
            <h2 class="text-xl font-bold text-text-light dark:text-text-dark mb-4">Gerenciamento de Tipos de Serviço</h2>
            <ServiceManagement />
          </div>

          <!-- Seção de Gerenciamento de Usuários -->
          <div class="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6 mb-8">
            <h2 class="text-xl font-bold text-text-light dark:text-text-dark mb-4">Gerenciamento de Usuários</h2>
            <UserManagement />
          </div>

        </div>
      </main>
    </div>
  </div>
</template>

<script>
import TopBar from '../components/TopBar.vue'
import Sidebar from '../components/Sidebar.vue'
import ServiceManagement from '../components/ServiceManagement.vue'
import UserManagement from '../components/UserManagement.vue' // Importar o componente de gerenciamento de usuários

export default {
  name: 'Configuracoes',
  components: {
    TopBar,
    Sidebar,
    ServiceManagement,
    UserManagement // Registrar o componente
  }
}
</script>

<style scoped>
/* Estilos específicos se necessário */
</style>
