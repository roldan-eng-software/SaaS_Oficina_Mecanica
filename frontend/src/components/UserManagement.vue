<template>
  <div>
    <div class="mb-6 flex justify-between items-center">
      <h3 class="text-lg font-bold text-text-light dark:text-text-dark">Usuários Cadastrados</h3>
      <button @click="$router.push({ name: 'Register' })" class="flex items-center gap-2 bg-primary text-white px-4 py-2 rounded-lg hover:opacity-90 transition-opacity">
        <span class="material-symbols-outlined">person_add</span>
        <span>Adicionar Novo Usuário</span>
      </button>
    </div>

    <div v-if="loading" class="p-4 text-center text-text-muted-light dark:text-text-muted-dark">
      Carregando usuários...
    </div>

    <div v-else-if="users.length === 0" class="p-4 text-center text-text-muted-light dark:text-text-muted-dark">
      Nenhum usuário cadastrado.
    </div>

    <div v-else class="overflow-x-auto bg-white dark:bg-gray-900 rounded-lg border border-gray-200 dark:border-gray-800">
      <table class="w-full">
        <thead class="bg-gray-50 dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Usuário</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Email</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Telefone</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Admin</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Ativo</th>
            <th class="px-6 py-3 text-right text-xs font-medium text-text-muted-light dark:text-text-muted-dark uppercase tracking-wider">Ações</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 dark:divide-gray-700">
          <tr v-for="user in users" :key="user.id" class="hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-text-light dark:text-text-dark">{{ user.username }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-text-muted-light dark:text-text-muted-dark">{{ user.email }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-text-muted-light dark:text-text-muted-dark">{{ user.telefone || '-' }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span v-if="user.is_staff" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400">Sim</span>
              <span v-else class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400">Não</span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span v-if="user.is_active" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400">Sim</span>
              <span v-else class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400">Não</span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="openEditModal(user)" class="text-primary hover:text-primary/80 mr-3">Editar</button>
              <button @click="deleteUser(user.id)" class="text-red-600 hover:text-red-700 dark:text-red-400 dark:hover:text-red-300">Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Add/Edit User Modal -->
    <Modal :show="showModal" @close="closeModal">
      <div class="p-6">
        <h2 class="text-2xl font-bold text-text-light dark:text-text-dark mb-4">Editar Usuário</h2>
        <form @submit.prevent="saveUser" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="username">Nome de Usuário</label>
            <input v-model="form.username" required class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="username" type="text" :disabled="true" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="email">Email</label>
            <input v-model="form.email" required class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="email" type="email" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="first_name">Primeiro Nome</label>
            <input v-model="form.first_name" class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="first_name" type="text" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="last_name">Sobrenome</label>
            <input v-model="form.last_name" class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="last_name" type="text" />
          </div>
          <div>
            <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="telefone">Telefone</label>
            <input v-model="form.telefone" class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="telefone" type="tel" />
          </div>
          <div class="flex items-center gap-4">
            <input v-model="form.is_staff" type="checkbox" id="is_staff" class="h-4 w-4 rounded border-gray-300 text-primary focus:ring-primary dark:border-gray-600 dark:bg-gray-700">
            <label for="is_staff" class="text-sm font-medium text-text-light dark:text-text-dark">Administrador</label>
          </div>
          <div class="flex items-center gap-4">
            <input v-model="form.is_active" type="checkbox" id="is_active" class="h-4 w-4 rounded border-gray-300 text-primary focus:ring-primary dark:border-gray-600 dark:bg-gray-700">
            <label for="is_active" class="text-sm font-medium text-text-light dark:text-text-dark">Ativo</label>
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
import Modal from './Modal.vue'

export default {
  name: 'UserManagement',
  components: {
    Modal
  },
  data() {
    return {
      users: [],
      loading: true,
      showModal: false,
      editingUser: null, // Armazena o usuário que está sendo editado
      form: {
        id: null,
        username: '',
        email: '',
        first_name: '',
        last_name: '',
        telefone: '',
        is_staff: false,
        is_active: false
      }
    }
  },
  async created() {
    await this.loadUsers()
  },
  methods: {
    async loadUsers() {
      this.loading = true
      try {
        const response = await api.get('/users/') // Endpoint para todos os usuários
        this.users = response.data
      } catch (err) {
        console.error("Erro ao carregar usuários:", err)
        alert('Erro ao carregar usuários.')
      } finally {
        this.loading = false
      }
    },
    openEditModal(user) {
      this.editingUser = user
      this.form = { ...user } // Copia os dados do usuário para o formulário
      this.showModal = true
    },
    closeModal() {
      this.showModal = false
    },
    async saveUser() {
      try {
        await api.patch(`/users/${this.form.id}/`, this.form)
        this.closeModal()
        await this.loadUsers() // Recarregar a lista após salvar
      } catch (err) {
        console.error("Erro ao salvar usuário:", err)
        alert('Erro ao salvar usuário.')
      }
    },
    async deleteUser(id) {
      if (confirm('Tem certeza que deseja excluir este usuário?')) {
        try {
          await api.delete(`/users/${id}/`)
          await this.loadUsers() // Recarregar a lista após excluir
        } catch (err) {
          console.error("Erro ao excluir usuário:", err)
          alert('Erro ao excluir usuário.')
        }
      }
    }
  }
}
</script>