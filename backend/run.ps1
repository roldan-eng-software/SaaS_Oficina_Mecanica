<#
Script: run.ps1
Uso: Executa os passos iniciais no Windows PowerShell para criar venv, instalar dependências e iniciar o servidor Django em modo dev.
Rodar como: .\run.ps1
#>

param(
    [switch]$NoInstall
)

Write-Host "Criando ambiente virtual .venv..."
python -m venv .venv

Write-Host "Ativando ambiente virtual..."
.
\.venv\Scripts\Activate.ps1

if (-not $NoInstall) {
    Write-Host "Instalando dependências..."
    pip install --upgrade pip
    pip install -r requirements.txt
}

Write-Host "Aplicando migrações..."
python manage.py migrate

Write-Host "Criando superuser (opcional)..."
Write-Host "Se quiser pular, pressione ENTER sem preencher usuário." -ForegroundColor Yellow
python manage.py createsuperuser

Write-Host "Iniciando servidor de desenvolvimento: http://127.0.0.1:8000"
python manage.py runserver
