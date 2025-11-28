<template>
  <div class="flex h-screen bg-background-light dark:bg-background-dark overflow-hidden">
    <!-- Sidebar -->
    <Sidebar />

    <!-- Main Content -->
    <div class="flex-1 flex flex-col overflow-hidden">
      <!-- TopBar -->
      <TopBar title="Dashboard" subtitle="Visão geral dos agendamentos" />

      <!-- Content Area -->
      <main class="flex-1 overflow-y-auto p-6">
        <!-- Stats Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <StatCard
            label="Total de Agendamentos"
            :value="stats.total"
            icon="event"
            :change="`${stats.total} no total`"
            trend="neutral"
          />
          <StatCard
            label="Pendentes"
            :value="stats.pendentes"
            icon="schedule"
            :change="`${stats.pendentes} aguardando confirmação`"
            trend="neutral"
          />
          <StatCard
            label="Confirmados"
            :value="stats.confirmados"
            icon="check_circle"
            :change="`${stats.confirmados} confirmados`"
            trend="up"
          />
          <StatCard
            label="Concluídos"
            :value="stats.concluidos"
            icon="task_alt"
            :change="`${stats.concluidos} finalizados`"
            trend="up"
          />
        </div>

        <!-- Appointments List -->
        <div class="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800">
          <div class="p-6 border-b border-gray-200 dark:border-gray-800">
            <div class="flex items-center justify-between">
              <h3 class="text-lg font-bold text-text-light dark:text-text-dark">Agendamentos Recentes</h3>
              <div class="flex gap-2">
                <button
                  v-for="status in statusFilters"
                  :key="status.value"
                  @click="filterStatus = status.value"
                  class="px-4 py-2 rounded-lg text-sm font-medium transition-colors"
                  :class="filterStatus === status.value 
                    ? 'bg-primary text-white' 
                    : 'bg-gray-100 dark:bg-gray-800 text-text-light dark:text-text-dark hover:bg-gray-200 dark:hover:bg-gray-700'"
                >
                  {{ status.label }}
                </button>
              </div>
            </div>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full">
              <thead class="bg-gray-50 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Cliente</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Veículo</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Serviço</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Data</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Status</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Ações</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
                <tr v-for="servico in filteredServicos" :key="servico.id" class="hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors">
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-center">
                      <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center mr-3">
                        <span class="material-symbols-outlined text-primary">person</span>
                      </div>
                      <div>
                        <div class="text-sm font-medium text-text-light dark:text-text-dark">{{ servico.cliente }}</div>
                        <div class="text-sm text-text-muted-light dark:text-text-muted-dark">{{ servico.telefone }}</div>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-text-light dark:text-text-dark">
                    {{ servico.veiculo }}
                  </td>
                  <td class="px-6 py-4 text-sm text-text-light dark:text-text-dark max-w-xs truncate">
                    {{ servico.descricao }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-text-light dark:text-text-dark">
                    {{ formatDate(servico.data_agendada) }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full" :class="getStatusClass(servico.status)">
                      {{ getStatusLabel(servico.status) }}
                    </span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm">
                    <div class="flex gap-2">
                      <button
                        v-if="servico.status === 'PENDENTE'"
                        @click="updateStatus(servico.id, 'CONFIRMADO')"
                        class="text-green-600 hover:text-green-700 dark:text-green-400 dark:hover:text-green-300"
                        title="Confirmar"
                      >
                        <span class="material-symbols-outlined text-lg">check_circle</span>
                      </button>
                      <button
                        v-if="servico.status === 'CONFIRMADO'"
                        @click="updateStatus(servico.id, 'EM_ANDAMENTO')"
                        class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300"
                        title="Iniciar"
                      >
                        <span class="material-symbols-outlined text-lg">play_circle</span>
                      </button>
                      <button
                        v-if="servico.status === 'EM_ANDAMENTO'"
                        @click="updateStatus(servico.id, 'CONCLUIDO')"
                        class="text-primary hover:opacity-80"
                        title="Concluir"
                      >
                        <span class="material-symbols-outlined text-lg">task_alt</span>
                      </button>
                      <button
                        v-if="['PENDENTE', 'CONFIRMADO'].includes(servico.status)"
                        @click="updateStatus(servico.id, 'CANCELADO')"
                        class="text-red-600 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300"
                        title="Cancelar"
                      >
                        <span class="material-symbols-outlined text-lg">cancel</span>
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <div v-if="filteredServicos.length === 0" class="p-12 text-center">
            <span class="material-symbols-outlined text-6xl text-gray-300 dark:text-gray-600 mb-4">event_busy</span>
            <p class="text-text-muted-light dark:text-text-muted-dark">Nenhum agendamento encontrado</p>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import api from '../services/api'
import Sidebar from '../components/Sidebar.vue'
import TopBar from '../components/TopBar.vue'
import StatCard from '../components/StatCard.vue'

export default {
  name: 'Home',
  components: {
    Sidebar,
    TopBar,
    StatCard
  },
  data() {
    return {
      servicos: [],
      filterStatus: 'TODOS'
    }
  },
  computed: {
    stats() {
      return {
        total: this.servicos.length,
        pendentes: this.servicos.filter(s => s.status === 'PENDENTE').length,
        confirmados: this.servicos.filter(s => s.status === 'CONFIRMADO').length,
        concluidos: this.servicos.filter(s => s.status === 'CONCLUIDO').length
      }
    },
    statusFilters() {
      return [
        { label: 'Todos', value: 'TODOS' },
        { label: 'Pendentes', value: 'PENDENTE' },
        { label: 'Confirmados', value: 'CONFIRMADO' },
        { label: 'Em Andamento', value: 'EM_ANDAMENTO' },
        { label: 'Concluídos', value: 'CONCLUIDO' }
      ]
    },
    filteredServicos() {
      if (this.filterStatus === 'TODOS') {
        return this.servicos
      }
      return this.servicos.filter(s => s.status === this.filterStatus)
    }
  },
  async created() {
    await this.loadServicos()
  },
  methods: {
    async loadServicos() {
      try {
        const r = await api.get('/servicos/')
        this.servicos = r.data
      } catch (err) {
        console.error(err)
      }
    },
    async updateStatus(id, newStatus) {
      try {
        await api.patch(`/servicos/${id}/`, { status: newStatus })
        await this.loadServicos()
      } catch (err) {
        console.error(err)
        alert('Erro ao atualizar status')
      }
    },
    formatDate(dateString) {
      if (!dateString) return '-'
      const date = new Date(dateString)
      return date.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' })
    },
    getStatusLabel(status) {
      const labels = {
        'PENDENTE': 'Pendente',
        'CONFIRMADO': 'Confirmado',
        'EM_ANDAMENTO': 'Em Andamento',
        'CONCLUIDO': 'Concluído',
        'CANCELADO': 'Cancelado'
      }
      return labels[status] || status
    },
    getStatusClass(status) {
      const classes = {
        'PENDENTE': 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400',
        'CONFIRMADO': 'bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400',
        'EM_ANDAMENTO': 'bg-purple-100 text-purple-800 dark:bg-purple-900/30 dark:text-purple-400',
        'CONCLUIDO': 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400',
        'CANCELADO': 'bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400'
      }
      return classes[status] || 'bg-gray-100 text-gray-800'
    }
  }
}
</script>

<style scoped>
/* Additional styles if needed */
</style>
