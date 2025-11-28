from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'Profile de {self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Servico(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='servicos')
    cliente = models.CharField(max_length=200)
    veiculo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_agendada = models.DateTimeField(null=True, blank=True)
    
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADO', 'Confirmado'),
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='Valor do serviço em R$')
    concluido = models.BooleanField(default=False) # Mantido por compatibilidade, será removido futuramente

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

class TipoServico(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    preco_sugerido = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = "Tipo de Serviço"
        verbose_name_plural = "Tipos de Serviços"
        ordering = ['nome']

    def __str__(self):
        return self.nome

