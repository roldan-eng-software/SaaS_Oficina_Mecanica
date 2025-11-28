<template>
  <div class="bg-white dark:bg-gray-900 p-8 rounded-xl border border-gray-200 dark:border-gray-800">
    <form @submit.prevent="submit" class="grid grid-cols-1 sm:grid-cols-2 gap-6">
      <div>
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="name">Nome Completo</label>
        <input v-model="form.name" required class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="name" placeholder="Digite seu nome completo" type="text" />
      </div>
      <div>
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="email">Email</label>
        <input v-model="form.email" required class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="email" placeholder="seuemail@exemplo.com" type="email" />
      </div>
      <div>
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="phone">Telefone</label>
        <input v-model="form.phone" required class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="phone" placeholder="(00) 90000-0000" type="tel" />
      </div>
      <div>
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="vehicle">Veículo (Marca/Modelo)</label>
        <input v-model="form.vehicle" class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="vehicle" placeholder="Ex: Toyota Corolla" type="text" />
      </div>
      <div>
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="service">Serviço Desejado</label>
        <select v-model="form.service" class="w-full rounded-lg border-gray-300 dark:border-gray-700 bg-background-light dark:bg-gray-800 text-text-light dark:text-text-dark focus:border-primary focus:ring-primary" id="service" required>
          <option disabled value="">Selecione um serviço</option>
          <option v-for="tipo in tiposServico" :key="tipo.id" :value="tipo.nome">{{ tipo.nome }}</option>
        </select>
      </div>
      <div class="sm:col-span-2">
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="date">Data e Hora Preferenciais</label>
        <input v-model="form.date" required class="w-full rounded-lg border-gray-300 dark:border-gray-700 bg-background-light dark:bg-gray-800 text-text-light dark:text-text-dark focus:border-primary focus:ring-primary" id="date" type="datetime-local" />
      </div>
      <div class="sm:col-span-2">
        <button :disabled="submitting" class="w-full flex min-w-[84px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-12 px-5 bg-primary text-white text-base font-bold leading-normal tracking-[0.015em] hover:opacity-90 transition-opacity" type="submit">
          <span class="truncate">Enviar Agendamento</span>
        </button>
      </div>
    </form>
    <div v-if="message" class="mt-4 p-3 rounded-md" :class="{'bg-green-50 text-green-800': messageType==='success','bg-red-50 text-red-800': messageType==='error'}">{{ message }}</div>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'AgendamentoForm',
  props: {
    userData: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      form: {
        name: '',
        email: '',
        phone: '',
        vehicle: '',
        service: '', // Alterado para string vazia
        date: ''
      },
      tiposServico: [], // Adicionado para armazenar os tipos de serviço
      submitting: false,
      message: null,
      messageType: 'success'
    }
  },
  watch: {
    userData: {
      handler(newVal) {
        if (newVal) {
          this.form.name = newVal.first_name || newVal.username || ''
          this.form.email = newVal.email || ''
          this.form.phone = newVal.telefone || '' // Preencher telefone se disponível
        }
      },
      immediate: true,
      deep: true
    }
  },
  async created() {
    await this.loadTiposServico()
  },
  methods: {
    async loadTiposServico() {
      try {
        const response = await api.get('/tipos-servico/')
        this.tiposServico = response.data
        if (this.tiposServico.length > 0) {
            this.form.service = this.tiposServico[0].nome; // Selecionar o primeiro como padrão, ou deixar vazio
        }
      } catch (err) {
        console.error("Erro ao carregar tipos de serviço:", err)
      }
    },
    async submit() {
      this.message = null
      if (!this.form.name || !this.form.email || !this.form.date || !this.form.service) { // Incluir validação para service
        this.messageType = 'error'
        this.message = 'Preencha todos os campos obrigatórios.'
        return
      }
      this.submitting = true
      try {
        const payload = {
          cliente: this.form.name,
          veiculo: this.form.vehicle || '-',
          descricao: `Serviço: ${this.form.service}`, // Usa o nome do serviço selecionado
          telefone: this.form.phone,
          email: this.form.email,
          data_agendada: this.form.date
        }
        const skipAuth = !this.userData || !this.userData.id
        await api.post('/servicos/', payload, { skipAuth: skipAuth })
        
        this.messageType = 'success'
        this.message = 'Agendamento enviado com sucesso. Entraremos em contato para confirmar.'
        
        this.$emit('submit-success')

        this.form.vehicle = ''
        this.form.date = ''
        if (!this.userData || !this.userData.id) {
          this.form.name = ''
          this.form.email = ''
          this.form.phone = ''
        }
        this.form.service = this.tiposServico.length > 0 ? this.tiposServico[0].nome : '' // Manter o serviço selecionado ou redefinir para o primeiro
        
      } catch (err) {
        console.error(err)
        this.messageType = 'error'
        this.message = 'Erro ao enviar agendamento. Tente novamente.'
      } finally {
        this.submitting = false
      }
    }
  }
}
</script>
