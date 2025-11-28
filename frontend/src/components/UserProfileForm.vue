<template>
  <div class="bg-white dark:bg-gray-900 p-8 rounded-xl border border-gray-200 dark:border-gray-800">
    <form @submit.prevent="submit" class="grid grid-cols-1 gap-6">
      <div>
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="first_name">Nome</label>
        <input v-model="form.first_name" class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="first_name" type="text" />
      </div>
      <div>
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="last_name">Sobrenome</label>
        <input v-model="form.last_name" class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="last_name" type="text" />
      </div>
      <div>
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="email">Email</label>
        <input v-model="form.email" required class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="email" type="email" />
      </div>
      <div>
        <label class="block text-sm font-medium text-text-light dark:text-text-dark mb-2" for="telefone">Telefone</label>
        <input v-model="form.telefone" class="form-input flex w-full resize-none overflow-hidden rounded-lg text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary/50 border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 focus:border-primary dark:focus:border-primary h-12 placeholder:text-gray-400 dark:placeholder:text-gray-500 px-4 text-base font-normal" id="telefone" type="tel" />
      </div>
      <div>
        <button :disabled="submitting" class="w-full flex min-w-[84px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-12 px-5 bg-primary text-white text-base font-bold leading-normal tracking-[0.015em] hover:opacity-90 transition-opacity" type="submit">
          <span class="truncate">Salvar Alterações</span>
        </button>
      </div>
    </form>
    <div v-if="message" class="mt-4 p-3 rounded-md" :class="{'bg-green-50 text-green-800': messageType==='success','bg-red-50 text-red-800': messageType==='error'}">{{ message }}</div>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'UserProfileForm',
  props: {
    userData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      form: {
        first_name: '',
        last_name: '',
        email: '',
        telefone: ''
      },
      submitting: false,
      message: null,
      messageType: 'success'
    }
  },
  watch: {
    userData: {
      handler(newVal) {
        if (newVal) {
          this.form.first_name = newVal.first_name || ''
          this.form.last_name = newVal.last_name || ''
          this.form.email = newVal.email || ''
          this.form.telefone = newVal.telefone || ''
        }
      },
      immediate: true,
      deep: true
    }
  },
  methods: {
    async submit() {
      this.message = null
      this.submitting = true
      try {
        await api.patch('/users/me/', this.form)
        this.messageType = 'success'
        this.message = 'Perfil atualizado com sucesso!'
        this.$emit('profile-updated') // Emitir evento de sucesso
      } catch (err) {
        console.error("Erro ao atualizar perfil:", err)
        this.messageType = 'error'
        this.message = 'Erro ao atualizar perfil. Tente novamente.'
      } finally {
        this.submitting = false
      }
    }
  }
}
</script>