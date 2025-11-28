from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_appointment_created_email(servico):
    """
    Send email notification when a new appointment is created.
    """
    if not servico.email:
        return  # Skip if no email provided
    
    subject = f'Agendamento Confirmado - AutoExpert'
    
    message = f"""
Olá {servico.cliente},

Seu agendamento foi recebido com sucesso!

Detalhes do Agendamento:
- Veículo: {servico.veiculo}
- Serviço: {servico.descricao}
- Data/Hora: {servico.data_agendada.strftime('%d/%m/%Y às %H:%M') if servico.data_agendada else 'A definir'}
- Status: Pendente

Entraremos em contato em breve para confirmar o horário.

Atenciosamente,
Equipe AutoExpert
    """.strip()
    
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[servico.email],
            fail_silently=False,
        )
        print(f"✅ Email enviado para {servico.email}")
    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}")


def send_status_change_email(servico, old_status, new_status):
    """
    Send email notification when appointment status changes.
    """
    if not servico.email:
        return  # Skip if no email provided
    
    status_messages = {
        'CONFIRMADO': 'confirmado',
        'EM_ANDAMENTO': 'iniciado',
        'CONCLUIDO': 'concluído',
        'CANCELADO': 'cancelado'
    }
    
    status_text = status_messages.get(new_status, new_status)
    
    subject = f'Atualização do Agendamento - AutoExpert'
    
    message = f"""
Olá {servico.cliente},

O status do seu agendamento foi atualizado!

Detalhes do Agendamento:
- Veículo: {servico.veiculo}
- Serviço: {servico.descricao}
- Novo Status: {status_text.upper()}

{_get_status_specific_message(new_status)}

Atenciosamente,
Equipe AutoExpert
    """.strip()
    
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[servico.email],
            fail_silently=False,
        )
        print(f"✅ Email de atualização enviado para {servico.email}")
    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}")


def _get_status_specific_message(status):
    """
    Get status-specific message for email.
    """
    messages = {
        'CONFIRMADO': 'Seu agendamento foi confirmado! Aguardamos você na data e hora marcadas.',
        'EM_ANDAMENTO': 'Seu veículo está sendo atendido neste momento. Em breve estará pronto!',
        'CONCLUIDO': 'Seu veículo está pronto para retirada! Obrigado por confiar em nossos serviços.',
        'CANCELADO': 'Seu agendamento foi cancelado. Entre em contato conosco se tiver dúvidas.'
    }
    return messages.get(status, '')
