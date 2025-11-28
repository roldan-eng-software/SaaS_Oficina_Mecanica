from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Servico
from .emails import send_appointment_created_email, send_status_change_email


# Store original status before save
@receiver(pre_save, sender=Servico)
def store_original_status(sender, instance, **kwargs):
    """
    Store the original status before saving to detect changes.
    """
    if instance.pk:  # Only for existing instances
        try:
            instance._original_status = Servico.objects.get(pk=instance.pk).status
        except Servico.DoesNotExist:
            instance._original_status = None
    else:
        instance._original_status = None


@receiver(post_save, sender=Servico)
def send_appointment_notifications(sender, instance, created, **kwargs):
    """
    Send email notifications when appointment is created or status changes.
    """
    if created:
        # New appointment created
        send_appointment_created_email(instance)
    else:
        # Existing appointment updated - check if status changed
        original_status = getattr(instance, '_original_status', None)
        if original_status and original_status != instance.status:
            send_status_change_email(instance, original_status, instance.status)
