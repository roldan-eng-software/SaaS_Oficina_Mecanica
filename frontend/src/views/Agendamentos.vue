<template>
  <div class="flex h-screen bg-background-light dark:bg-background-dark overflow-hidden">
    <!-- Sidebar -->
    <Sidebar />

    <!-- Main Content -->
    <div class="flex-1 flex flex-col overflow-hidden">
      <!-- TopBar -->
      <TopBar title="Agendamentos" subtitle="Gerencie todos os agendamentos da oficina" />

      <!-- Content Area -->
      <main class="flex-1 overflow-y-auto p-6">
        <!-- Actions Bar -->
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6">
          <!-- Search -->
          <div class="relative w-full sm:w-96">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <span class="material-symbols-outlined text-gray-400">search</span>
            </div>
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Buscar por cliente ou veículo..."
              class="block w-full pl-10 pr-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-text-light dark:text-text-dark placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
            />
          </div>

          <!-- Add Button -->
          <button
            @click="openCreateModal"
            class="flex items-center gap-2 px-4 py-2 bg-primary text-white rounded-lg hover:opacity-90 transition-opacity whitespace-nowrap"
          >
            <span class="material-symbols-outlined">add</span>
            Novo Agendamento
          </button>
        </div>

        <!-- Filters -->
        <div class="flex gap-2 mb-6 overflow-x-auto pb-2">
          <button
            v-for="status in statusFilters"
            :key="status.value"
            @click="filterStatus = status.value"
            class="px-4 py-2 rounded-lg text-sm font-medium transition-colors whitespace-nowrap"
            :class="filterStatus === status.value 
              ? 'bg-primary text-white' 
              : 'bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 text-text-light dark:text-text-dark hover:bg-gray-50 dark:hover:bg-gray-800'"
          >
            {{ status.label }}
          </button>
        </div>

        <!-- Table -->
        <div class="bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 overflow-hidden">
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
                    <div>
                      <div class="text-sm font-medium text-text-light dark:text-text-dark">{{ servico.cliente }}</div>
                      <div class="text-sm text-text-muted-light dark:text-text-muted-dark">{{ servico.telefone || '-' }}</div>
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
                        @click="openEditModal(servico)"
                        class="text-blue-600 hover:text-blue-700 dark:text-blue-400 dark:hover:text-blue-300"
                        title="Editar"
                      >
                        <span class="material-symbols-outlined text-lg">edit</span>
                      </button>
                      <button
                        @click="openDeleteModal(servico)"
                        class="text-red-600 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300"
                        title="Excluir"
                      >
                        <span class="material-symbols-outlined text-lg">delete</span>
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

    <!-- Create/Edit Modal -->
    <Modal
      :show="showFormModal"
      :title="isEditing ? 'Editar Agendamento' : 'Novo Agendamento'"
      :loading="formLoading"
      :confirm-text="isEditing ? 'Salvar' : 'Criar'"
      @close="closeFormModal"
      @confirm="submitForm"
    >
      <form @submit.prevent="submitForm" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2">Cliente *</label>
          <input
            v-model="form.cliente"
            required
            type="text"
            class="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:ring-2 focus:ring-primary focus:border-transparent"
            placeholder="Nome do cliente"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2">Telefone</label>
          <input
            v-model="form.telefone"
            type="tel"
            class="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:ring-2 focus:ring-primary focus:border-transparent"
            placeholder="(00) 00000-0000"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2">Email</label>
          <input
            v-model="form.email"
            type="email"
            class="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:ring-2 focus:ring-primary focus:border-transparent"
            placeholder="email@exemplo.com"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2">Veículo *</label>
          <input
            v-model="form.veiculo"
            required
            type="text"
            class="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:ring-2 focus:ring-primary focus:border-transparent"
            placeholder="Marca/Modelo"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2">Descrição do Serviço *</label>
          <textarea
            v-model="form.descricao"
            required
            rows="3"
            class="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:ring-2 focus:ring-primary focus:border-transparent"
            placeholder="Descreva o serviço a ser realizado"
          ></textarea>
        </div>

        <div>
          <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2">Data e Hora *</label>
          <input
            v-model="form.data_agendada"
            required
            type="datetime-local"
            class="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:ring-2 focus:ring-primary focus:border-transparent"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2">Status</label>
          <select
            v-model="form.status"
            class="w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:ring-2 focus:ring-primary focus:border-transparent"
          >
            <option value="PENDENTE">Pendente</option>
            <option value="CONFIRMADO">Confirmado</option>
            <option value="EM_ANDAMENTO">Em Andamento</option>
            <option value="CONCLUIDO">Concluído</option>
            <option value="CANCELADO">Cancelado</option>
          </select>
        </div>
      </form>
    </Modal>

    <!-- Delete Confirmation Modal -->
    <Modal
      :show="showDeleteModal"
      title="Confirmar Exclusão"
      :loading="deleteLoading"
      confirm-text="Excluir"
      cancel-text="Cancelar"
      @close="closeDeleteModal"
      @confirm="confirmDelete"
    >
      <p class="text-text-light dark:text-text-dark">
        Tem certeza que deseja excluir o agendamento de <strong>{{ selectedServico?.cliente }}</strong>?
      </p>
      <p class="text-sm text-text-muted-light dark:text-text-muted-dark mt-2">
        Esta ação não pode ser desfeita.
      </p>
    </Modal>
  </div>
</template>

<script>
import api from '../services/api'
import Sidebar from '../components/Sidebar.vue'
import TopBar from '../components/TopBar.vue'
import Modal from '../components/Modal.vue'

export default {
  name: 'Agendamentos',
  components: {
    Sidebar,
    TopBar,
    Modal
  },
  data() {
    return {
      servicos: [],
      searchQuery: '',
      filterStatus: 'TODOS',
      showFormModal: false,
      showDeleteModal: false,
      isEditing: false,
      formLoading: false,
      deleteLoading: false,
      selectedServico: null,
      form: {
        cliente: '',
        telefone: '',
        email: '',
        veiculo: '',
        descricao: '',
        data_agendada: '',
        status: 'PENDENTE'
      }
    }
  },
  computed: {
    statusFilters() {
      return [
        { label: 'Todos', value: 'TODOS' },
        { label: 'Pendentes', value: 'PENDENTE' },
        { label: 'Confirmados', value: 'CONFIRMADO' },
        { label: 'Em Andamento', value: 'EM_ANDAMENTO' },
        { label: 'Concluídos', value: 'CONCLUIDO' },
        { label: 'Cancelados', value: 'CANCELADO' }
      ]
    },
    filteredServicos() {
      let result = this.servicos

      // Filter by status
      if (this.filterStatus !== 'TODOS') {
        result = result.filter(s => s.status === this.filterStatus)
      }

      // Filter by search query
      if (this.searchQuery.trim()) {
        const query = this.searchQuery.toLowerCase()
        result = result.filter(s => 
          s.cliente.toLowerCase().includes(query) ||
          s.veiculo.toLowerCase().includes(query) ||
          (s.telefone && s.telefone.toLowerCase().includes(query))
        )
      }

      return result
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
    openCreateModal() {
      this.isEditing = false
      this.form = {
        cliente: '',
        telefone: '',
        email: '',
        veiculo: '',
        descricao: '',
        data_agendada: '',
        status: 'PENDENTE'
      }
      this.showFormModal = true
    },
    openEditModal(servico) {
      this.isEditing = true
      this.selectedServico = servico
      this.form = {
        cliente: servico.cliente,
        telefone: servico.telefone || '',
        email: servico.email || '',
        veiculo: servico.veiculo,
        descricao: servico.descricao,
        data_agendada: servico.data_agendada ? servico.data_agendada.slice(0, 16) : '',
        status: servico.status
      }
      this.showFormModal = true
    },
    closeFormModal() {
      this.showFormModal = false
      this.selectedServico = null
    },
    async submitForm() {
      this.formLoading = true
      try {
        if (this.isEditing) {
          await api.patch(`/servicos/${this.selectedServico.id}/`, this.form)
        } else {
          await api.post('/servicos/', this.form)
        }
        await this.loadServicos()
        this.closeFormModal()
      } catch (err) {
        console.error(err)
        alert('Erro ao salvar agendamento')
      } finally {
        this.formLoading = false
      }
    },
    openDeleteModal(servico) {
      this.selectedServico = servico
      this.showDeleteModal = true
    },
    closeDeleteModal() {
      this.showDeleteModal = false
      this.selectedServico = null
    },
    async confirmDelete() {
      this.deleteLoading = true
      try {
        await api.delete(`/servicos/${this.selectedServico.id}/`)
        await this.loadServicos()
        this.closeDeleteModal()
      } catch (err) {
        console.error(err)
        alert('Erro ao excluir agendamento')
      } finally {
        this.deleteLoading = false
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
