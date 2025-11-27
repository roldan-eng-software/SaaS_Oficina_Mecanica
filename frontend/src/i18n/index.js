import { createI18n } from 'vue-i18n'

const messages = {
  'pt-BR': {
    login: {
      title: 'Entrar',
      username: 'Usuário',
      password: 'Senha',
      submit: 'Entrar',
      noAccount: 'Criar uma conta'
    },
    register: {
      title: 'Registrar',
      username: 'Usuário',
      email: 'E-mail',
      password: 'Senha',
      submit: 'Registrar',
      haveAccount: 'Já tem conta? Entre'
    },
    home: {
      title: 'Painel da Oficina',
      logout: 'Sair'
    }
  }
}

const i18n = createI18n({
  legacy: false,
  locale: 'pt-BR',
  messages
})

export default i18n
