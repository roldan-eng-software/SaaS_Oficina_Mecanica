<template>
  <div class="flex flex-col h-screen bg-background-light dark:bg-background-dark">
    <!-- TopBar -->
    <ClientTopBar />

    <!-- Main Content -->
    <main class="flex-1 overflow-y-auto p-6">
      <div class="max-w-6xl mx-auto">
        <!-- Welcome Section -->
        <div class="mb-8 flex justify-between items-start">
          <div>
            <h1 class="text-3xl font-bold text-text-light dark:text-text-dark mb-2">
              Bem-vindo, {{ userData.first_name || userData.username }}!
            </h1>
            <p class="text-text-muted-light dark:text-text-muted-dark">
              Aqui você pode acompanhar seus agendamentos e gerenciar seu perfil.
            </p>
            <p v-if="userData.email" class="text-text-muted-light dark:text-text-muted-dark text-sm mt-1">
              E-mail: {{ userData.email }}
            </p>
          </div>
          <button @click="showProfileModal = true" class="flex items-center gap-2 bg-gray-200 dark:bg-gray-700 text-text-light dark:text-text-dark px-4 py-2 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors">
            <span class="material-symbols-outlined">edit</span>
            <span>Editar Perfil</span>
          </button>
        </div>

        <div class="flex justify-between items-center mb-8">
          <div>
            <h2 class="text-3xl font-bold text-text-light dark:text-text-dark mb-2">Meus Agendamentos</h2>
            <p class="text-text-muted-light dark:text-text-muted-dark">Acompanhe o status dos seus serviços</p>
          </div>
          <button @click="showAgendamentoModal = true" class="flex items-center gap-2 bg-primary text-white px-4 py-2 rounded-lg hover:opacity-90 transition-opacity">
            <span class="material-symbols-outlined">add</span>
            <span>Novo Agendamento</span>
          </button>
        </div>

        <!-- Current Appointments -->
        <div v-if="currentAppointments.length > 0" class="mb-8">
          <h2 class="text-xl font-bold text-text-light dark:text-text-dark mb-4">Agendamentos Ativos</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div
              v-for="servico in currentAppointments"
              :key="servico.id"
              class="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 p-6"
            >
              <div class="flex items-start justify-between mb-4">
                <div class="flex-1">
                  <h3 class="text-lg font-bold text-text-light dark:text-text-dark mb-1">{{ servico.veiculo }}</h3>
                  <p class="text-sm text-text-muted-light dark:text-text-muted-dark">{{ formatDate(servico.data_agendada) }}</p>
                </div>
                <span class="px-3 py-1 text-xs font-semibold rounded-full" :class="getStatusClass(servico.status)">
                  {{ getStatusLabel(servico.status) }}
                </span>
              </div>

              <p class="text-sm text-text-light dark:text-text-dark mb-4">{{ servico.descricao }}</p>

              <!-- Status Timeline -->
              <div class="space-y-2">
                <div class="flex items-center gap-2">
                  <div class="w-6 h-6 rounded-full flex items-center justify-center" :class="servico.status === 'PENDENTE' ? 'bg-yellow-100 dark:bg-yellow-900/30' : 'bg-green-100 dark:bg-green-900/30'">
                    <span class="material-symbols-outlined text-xs" :class="servico.status === 'PENDENTE' ? 'text-yellow-600 dark:text-yellow-400' : 'text-green-600 dark:text-green-400'">
                      {{ servico.status === 'PENDENTE' ? 'schedule' : 'check' }}
                    </span>
                  </div>
                  <span class="text-xs text-text-muted-light dark:text-text-muted-dark">Solicitado</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-6 h-6 rounded-full flex items-center justify-center" :class="['CONFIRMADO', 'EM_ANDAMENTO', 'CONCLUIDO'].includes(servico.status) ? 'bg-green-100 dark:bg-green-900/30' : 'bg-gray-100 dark:bg-gray-800'">
                    <span class="material-symbols-outlined text-xs" :class="['CONFIRMADO', 'EM_ANDAMENTO', 'CONCLUIDO'].includes(servico.status) ? 'text-green-600 dark:text-green-400' : 'text-gray-400'">
                      {{ ['CONFIRMADO', 'EM_ANDAMENTO', 'CONCLUIDO'].includes(servico.status) ? 'check' : 'radio_button_unchecked' }}
                    </span>
                  </div>
                  <span class="text-xs text-text-muted-light dark:text-text-muted-dark">Confirmado</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-6 h-6 rounded-full flex items-center justify-center" :class="['EM_ANDAMENTO', 'CONCLUIDO'].includes(servico.status) ? 'bg-green-100 dark:bg-green-900/30' : 'bg-gray-100 dark:bg-gray-800'">
                    <span class="material-symbols-outlined text-xs" :class="['EM_ANDAMENTO', 'CONCLUIDO'].includes(servico.status) ? 'text-green-600 dark:text-green-400' : 'text-gray-400'">
                      {{ ['EM_ANDAMENTO', 'CONCLUIDO'].includes(servico.status) ? 'check' : 'radio_button_unchecked' }}
                    </span>
                  </div>
                  <span class="text-xs text-text-muted-light dark:text-text-muted-dark">Em Andamento</span>
                </div>
                <div class="flex items-center gap-2">
                  <div class="w-6 h-6 rounded-full flex items-center justify-center" :class="servico.status === 'CONCLUIDO' ? 'bg-green-100 dark:bg-green-900/30' : 'bg-gray-100 dark:bg-gray-800'">
                    <span class="material-symbols-outlined text-xs" :class="servico.status === 'CONCLUIDO' ? 'text-green-600 dark:text-green-400' : 'text-gray-400'">
                      {{ servico.status === 'CONCLUIDO' ? 'check' : 'radio_button_unchecked' }}
                    </span>
                  </div>
                  <span class="text-xs text-text-muted-light dark:text-text-muted-dark">Concluído</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- History -->
        <div>
          <h2 class="text-xl font-bold text-text-light dark:text-text-dark mb-4">Histórico</h2>
          <div class="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 overflow-hidden">
            <div v-if="historyAppointments.length === 0" class="p-12 text-center">
              <span class="material-symbols-outlined text-6xl text-gray-300 dark:text-gray-600 mb-4">history</span>
              <p class="text-text-muted-light dark:text-text-muted-dark">Nenhum histórico de serviços</p>
            </div>
            <div v-else class="overflow-x-auto">
              <table class="w-full">
                <thead class="bg-gray-50 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
                  <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Data</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Veículo</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Serviço</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Status</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
                  <tr v-for="servico in historyAppointments" :key="servico.id" class="hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors">
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-text-light dark:text-text-dark">
                      {{ formatDate(servico.data_agendada) }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-text-light dark:text-text-dark">
                      {{ servico.veiculo }}
                    </td>
                    <td class="px-6 py-4 text-sm text-text-light dark:text-text-dark max-w-xs truncate">
                      {{ servico.descricao }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full" :class="getStatusClass(servico.status)">
                        {{ getStatusLabel(servico.status) }}
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </main>
    <!-- Agendamento Modal -->
    <Modal :show="showAgendamentoModal" @close="showAgendamentoModal = false">
      <div class="p-6">
        <h2 class="text-2xl font-bold text-text-light dark:text-text-dark mb-4">Novo Agendamento</h2>
        <agendamento-form :user-data="userData" @submit-success="handleAgendamentoSuccess" />
      </div>
    </Modal>

    <!-- Editar Perfil Modal -->
    <Modal :show="showProfileModal" @close="showProfileModal = false">
      <div class="p-6">
        <h2 class="text-2xl font-bold text-text-light dark:text-text-dark mb-4">Editar Perfil</h2>
        <UserProfileForm :user-data="userData" @profile-updated="handleProfileUpdated" />
      </div>
    </Modal>
  </div>
</template>

<script>
import api from '../services/api'
import ClientTopBar from '../components/ClientTopBar.vue'
import AgendamentoForm from '../components/AgendamentoForm.vue'
import UserProfileForm from '../components/UserProfileForm.vue' // Importar UserProfileForm
import Modal from '../components/Modal.vue'

export default {
  name: 'ClienteDashboard',
  components: {
    ClientTopBar,
    AgendamentoForm,
    UserProfileForm, // Adicionar UserProfileForm
    Modal
  },
  data() {
    return {
      servicos: [],
      userData: {},
      showAgendamentoModal: false,
      showProfileModal: false // Adicionar showProfileModal
    }
  },
  computed: {
    currentAppointments() {
      return this.servicos.filter(s => ['PENDENTE', 'CONFIRMADO', 'EM_ANDAMENTO'].includes(s.status))
    },
    historyAppointments() {
      return this.servicos.filter(s => ['CONCLUIDO', 'CANCELADO'].includes(s.status))
    }
  },
  async created() {
    await this.loadUserData() // Chamar para carregar dados do usuário
    await this.loadServicos()
  },
  methods: {
    async loadUserData() { // Novo método para carregar dados do usuário
      try {
        const response = await api.get('/users/me/')
        this.userData = response.data
      } catch (err) {
        console.error("Erro ao carregar dados do usuário:", err)
        // Redirecionar para login se o token for inválido/expirado
        if (err.response && err.response.status === 401) {
          this.$router.push({ name: 'Login' })
        }
      }
    },
    async loadServicos() {
      try {
        const r = await api.get('/servicos/')
        // Backend now automatically filters by user
        this.servicos = r.data
      } catch (err) {
        console.error("Erro ao carregar serviços:", err)
      }
    },
    handleAgendamentoSuccess() {
      this.showAgendamentoModal = false
      this.loadServicos()
    },
    handleProfileUpdated() { // Novo método para lidar com atualização do perfil
      this.showProfileModal = false
      this.loadUserData() // Recarregar dados do usuário para refletir as mudanças
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
