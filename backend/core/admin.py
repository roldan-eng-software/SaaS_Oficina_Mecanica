from django.contrib import admin
from .models import Servico, Profile, TipoServico # Importar TipoServico


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'veiculo', 'data_agendada', 'concluido')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefone')
    search_fields = ('user__username', 'telefone')

@admin.register(TipoServico) # Registrar TipoServico
class TipoServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco_sugerido')
    search_fields = ('nome',)
