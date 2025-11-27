# Backend - Django (mínimo)

Este diretório contém um projeto Django mínimo configurado para desenvolvimento local e com `LANGUAGE_CODE = 'pt-br'`.

Passos rápidos (PowerShell - Windows):

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Também existe um script `run.ps1` que automatiza a criação do venv, instalação e execução:

```powershell
.\run.ps1
```

API mínima disponível:
- `GET /api/servicos/` - lista de serviços
- `POST /api/servicos/` - criar serviço

Autenticação / JWT:
- `POST /api/auth/token/` - obtém `access` e `refresh` tokens (login)
- `POST /api/auth/token/refresh/` - renova o `access` com o `refresh`
- `POST /api/auth/register/` - cria novo usuário (registro)
- `POST /api/auth/logout/` - faz blacklist do `refresh` token (logout)

Nota: o projeto agora usa cookies HttpOnly para armazenar o `refresh` token (mais seguro). Os endpoints atualizados são:
- `POST /api/auth/login/` - realiza login, retorna `access` no corpo e seta `refresh` como cookie HttpOnly
- `POST /api/auth/refresh/` - renova `access` usando o cookie HttpOnly `refresh` (não precisa enviar body)
- `POST /api/auth/register/` - cria novo usuário (registro)
- `POST /api/auth/logout/` - faz blacklist do `refresh` (lê cookie HttpOnly) e remove o cookie

Exemplo de logout (JSON):

```json
{
	"refresh": "<SEU_REFRESH_TOKEN_AQUI>"
}
```

Resposta: HTTP 205 Reset Content quando o refresh for validamente blacklistado.
