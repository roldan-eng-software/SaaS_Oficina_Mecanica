<template>
  <div>
    <div class="mb-6 flex justify-between items-center">
      <h3 class="text-lg font-bold text-text-light dark:text-text-dark">Tipos de Serviços Disponíveis</h3>
      <button @click="openAddModal" class="flex items-center gap-2 bg-primary text-white px-4 py-2 rounded-lg hover:opacity-90 transition-opacity">
        <span class="material-symbols-outlined">add</span>
        <span>Adicionar Novo Serviço</span>
      </button>
    </div>

    <div v-if="loading" class="p-4 text-center text-text-muted-light dark:text-text-muted-dark">
      Carregando tipos de serviço...
    </div>

    <div v-else-if="tiposServico.length === 0" class="p-4 text-center text-text-muted-light dark:text-text-muted-dark">
      Nenhum tipo de serviço cadastrado.
    </div>

    <div v-else class="overflow-x-auto bg-white dark:bg-gray-900 rounded-lg border border-gray-200 dark:border-gray-800">
      <table class="w-full">
        <thead class="bg-gray-50 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Nome</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Preço Sugerido (R$)</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Ações</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
          <tr v-for="tipo in tiposServico" :key="tipo.id" class="hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-text-light dark:text-text-dark">{{ tipo.nome }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-text-muted-light dark:text-text-muted-dark">{{ formatCurrency(tipo.preco_sugerido) }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="openEditModal(tipo)" class="text-primary hover:text-primary/80 mr-3">Editar</button>
              <button @click="deleteTipoServico(tipo.id)" class="text-red-600 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Add/Edit Service Modal -->
    <Modal :show="showModal" @close="closeModal">
      <div class="p-6">
        <h2 class="text-2xl font-bold text-text-light dark:text-text-dark mb-4">{{ editingTipoServico ? 'Editar Serviço' : 'Adicionar Novo Serviço' }}</h2>
        <form @submit.prevent="saveTipoServico" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="nome">Nome do Serviço</label>
            <input v-model="form.nome" required class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="nome" type="text" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="preco_sugerido">Preço Sugerido (R$)</label>
            <input v-model.number="form.preco_sugerido" class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="preco_sugerido" type="number" step="0.01" />
          </div>
          <div class="flex justify-end gap-3">
            <button type="button" @click="closeModal" class="px-4 py-2 rounded-lg text-sm font-medium text-text-light dark:text-text-dark bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors">
              Cancelar
            </button>
            <button type="submit" class="px-4 py-2 rounded-lg text-sm font-medium text-white bg-primary hover:opacity-90 transition-opacity">
              Salvar
            </button>
          </div>
        </form>
      </div>
    </Modal>
  </div>
</template>

<script>
import api from '../services/api'
import Modal from './Modal.vue' // Importar o componente Modal

export default {
  name: 'ServiceManagement',
  components: {
    Modal
  },
  data() {
    return {
      tiposServico: [],
      loading: true,
      showModal: false,
      editingTipoServico: null, // Armazena o tipo de serviço que está sendo editado (ou null para adicionar)
      form: {
        nome: '',
        preco_sugerido: null
      }
    }
  },
  async created() {
    await this.loadTiposServico()
  },
  methods: {
    async loadTiposServico() {
      this.loading = true
      try {
        const response = await api.get('/tipos-servico/')
        this.tiposServico = response.data
      } catch (err) {
        console.error("Erro ao carregar tipos de serviço:", err)
        alert('Erro ao carregar tipos de serviço.')
      } finally {
        this.loading = false
      }
    },
    openAddModal() {
      this.editingTipoServico = null
      this.form.nome = ''
      this.form.preco_sugerido = null
      this.showModal = true
    },
    openEditModal(tipo) {
      this.editingTipoServico = tipo
      this.form.nome = tipo.nome
      this.form.preco_sugerido = tipo.preco_sugerido
      this.showModal = true
    },
    closeModal() {
      this.showModal = false
    },
    async saveTipoServico() {
      try {
        if (this.editingTipoServico) {
          // Editar serviço existente
          await api.put(`/tipos-servico/${this.editingTipoServico.id}/`, this.form)
        } else {
          // Adicionar novo serviço
          await api.post('/tipos-servico/', this.form)
        }
        this.closeModal()
        await this.loadTiposServico() // Recarregar a lista após salvar
      } catch (err) {
        console.error("Erro ao salvar tipo de serviço:", err)
        alert('Erro ao salvar tipo de serviço.')
      }
    },
    async deleteTipoServico(id) {
      if (confirm('Tem certeza que deseja excluir este tipo de serviço?')) {
        try {
          await api.delete(`/tipos-servico/${id}/`)
          await this.loadTiposServico() // Recarregar a lista após excluir
        } catch (err) {
          console.error("Erro ao excluir tipo de serviço:", err)
          alert('Erro ao excluir tipo de serviço.')
        }
      }
    },
    formatCurrency(value) {
      if (value === null || value === undefined) return 'R$ -'
      return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value)
    }
  }
}
</script>