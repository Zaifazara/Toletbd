# Generated by Django 4.2.6 on 2023-11-19 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_ticket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
    ]