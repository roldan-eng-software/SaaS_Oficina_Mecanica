# SaaS Oficina Mecânica - Prompt para Agente VSCode

## 🎯 Objetivo do Projeto

Desenvolver uma solução SaaS completa para gerenciamento de oficinas mecânicas de automóveis, composta por uma Landing Page atrativa com agendamento online e um Sistema de Gestão Administrativo com múltiplos níveis de acesso.

---

## 📋 Especificações do Projeto

### **ETAPA 01: Landing Page**

**Funcionalidades Principais:**
- Página inicial atrativa e responsiva
- Formulário de cadastro de clientes
- Sistema de agendamento online integrado
- Notificações de status via WhatsApp
- Exibição de informações críticas no acesso à Landing Page:
  - Valor do orçamento do veículo
  - Data e horário da manutenção agendada
  - Status de conclusão do serviço

**Requisitos Técnicos:**
- Design moderno e intuitivo
- Integração com WhatsApp Business API
- Banco de dados para armazenar agendamentos
- Responsivo (Desktop, Tablet, Mobile)

---

### **ETAPA 02: Sistema SaaS - Área Administrativa**

#### **Módulo de Controle de Acesso**

**Níveis de Usuário:**
- **Administrador**: Acesso total ao sistema
- **Atendente**: Gerenciamento de clientes e agendamentos
- **Mecânico**: Visualização de ordens de serviço e atualização de status
- **Marketing**: Gerenciamento de campanhas e relatórios
- **Comprador**: Gestão de estoque e pedidos de peças

---

#### **Telas Obrigatórias do Sistema**

**A. Gestão de Usuários**
- Cadastro, edição e exclusão de usuários
- Atribuição de níveis de acesso (roles)
- Visualização de histórico de ações por usuário
- Ativação/Desativação de contas

**B. Gestão de Veículos**
- Cadastro de novos veículos
- Importação de dados via acesso online da Landing Page
- Cadastro manual local
- Histórico de manutenção por veículo
- Documentação (placa, chassi, modelo, ano, proprietário)

**C. Estoque de Peças**
- Cadastro de peças com código, descrição e preço
- Controle de quantidade disponível
- Alertas de estoque baixo
- Histórico de entrada e saída
- Fornecedores e contatos

**D. Agendamentos**
- Listagem de agendamentos (diários, semanais, mensais)
- Visualização de disponibilidade de mecânicos
- Confirmação e cancelamento de agendamentos
- Notificações automáticas ao cliente

**E. Financeiro**
- Emissão de orçamentos
- Registro de pagamentos recebidos
- Controle de contas a receber
- Relatórios de fluxo de caixa
- Dashboard com indicadores financeiros

**F. Contratos de Prestação de Serviço**
- Templates de contratos padronizados
- Geração automática de contratos por serviço
- Assinatura digital (integração com e-sign opcional)
- Arquivo e histórico de contratos

**G. Relatórios**
- Relatório de Produtividade (serviços realizados por mecânico, taxa de conclusão)
- Relatório Financeiro (receita, despesas, lucro)
- Relatório de Estoque (movimentação, itens críticos)
- Exportação em PDF e Excel

---

## 🛠️ Stack Tecnológico Sugerido

**Ambiente virtual**
- .venv

**GitHub**
- Criar repositório no GitHub

**Frontend:**
- Vue.js (com TypeScript)
- Tailwind CSS ou Material-UI
- State Management (Redux ou Pinia)

**Backend:**
- Django REST Framework (Python)

**Banco de Dados:**
- MySQL

**Autenticação:**
- JWT (JSON Web Tokens)

**Integrações Externas:**
- WhatsApp Business API
- Serviço de e-mail
- Gerador de PDF

---

## 📊 Fluxo de Usuário Resumido

1. **Cliente** acessa Landing Page → Cadastra-se → Agenda serviço → Recebe notificações WhatsApp
2. **Atendente** confirma agendamento → Cria ordem de serviço
3. **Mecânico** visualiza ordem → Realiza manutenção → Atualiza status
4. **Comprador** gerencia estoque de peças conforme demanda
5. **Marketing** monitora relatórios e cria estratégias
6. **Administrador** supervisiona tudo e gerencia permissões

---

## ✅ Checklist de Desenvolvimento

- [ ] Autenticação e autorização por níveis
- [ ] CRUD completo em todas as telas
- [ ] Integração WhatsApp
- [ ] Geração automática de relatórios
- [ ] Validação de dados em frontend e backend
- [ ] Tratamento de erros e logging
- [ ] Testes unitários e de integração
- [ ] Documentação de API (Swagger/OpenAPI)
- [ ] Deploy e CI/CD
- [ ] Backup e recuperação de dados

---

## 🎨 Notas Adicionais

- Priorizar usabilidade e velocidade
- Interface intuitiva para usuários não-técnicos
- Suportar múltiplas oficinas (multi-tenancy) se escalável
- Plano futuro: App mobile nativa
