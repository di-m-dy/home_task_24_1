# Generated by Django 5.1.2 on 2024-10-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата оплаты'),
        ),
    ]
