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

class Agendamento(models.Model):
    cliente = models.CharField(max_length=200)
    veiculo = models.CharField(max_length=200)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='agendamentos')
    data_agendada = models.DateTimeField(null=True, blank=True)
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADO', 'Confirmado'),
        ('CANCELADO', 'Cancelado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Agendamento {self.id} - {self.veiculo} ({self.cliente})"
