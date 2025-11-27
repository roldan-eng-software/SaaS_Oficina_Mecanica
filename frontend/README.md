# Frontend - Vite + Vue (mínimo)

Este diretório contém um scaffold mínimo em Vue 3 com Vite, `vue-router`, `axios` e `vue-i18n` configurados. O frontend consome a API Django no `http://127.0.0.1:8000/api`.

Instalação e execução (PowerShell - Windows):

```powershell
cd frontend
npm install
npm run dev
```

Observações:
- As chamadas API usam `http://127.0.0.1:8000/api` como `baseURL` — ajuste em `src/services/api.js` se necessário.
- O fluxo de autenticação utiliza JWT (access + refresh) e armazena tokens em `localStorage`.
- i18n está configurado para `pt-BR` em `src/i18n/index.js`.
