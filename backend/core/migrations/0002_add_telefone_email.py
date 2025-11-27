from django.db import migrations, models
import re


def extract_contact_info(apps, schema_editor):
    Servico = apps.get_model('core', 'Servico')
    email_re = re.compile(r"[\w\.-]+@[\w\.-]+")
    phone_re = re.compile(r"(\+?\d[\d\s().-]{5,}\d)")

    for serv in Servico.objects.all():
        descricao = serv.descricao or ''
        found_email = email_re.search(descricao)
        found_phone = phone_re.search(descricao)
        if found_email:
            serv.email = found_email.group(0)
            descricao = descricao.replace(found_email.group(0), '')
        if found_phone:
            serv.telefone = found_phone.group(0)
            descricao = descricao.replace(found_phone.group(0), '')
        # clean up leftover separators and whitespace
        serv.descricao = descricao.strip(' ,;:\n\t')
        serv.save()


def reverse_func(apps, schema_editor):
    # Não reverter: manter dados separados é desejável
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='telefone',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.RunPython(extract_contact_info, reverse_func),
    ]
