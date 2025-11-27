from django.db import models


class Servico(models.Model):
    cliente = models.CharField(max_length=200)
    veiculo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_agendada = models.DateTimeField(null=True, blank=True)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return f"Servico {self.id} - {self.veiculo} ({self.cliente})"
