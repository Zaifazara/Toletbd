# Generated by Django 4.2.6 on 2023-11-18 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0016_alter_property_radiocheck'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='radiocheck',
            new_name='name',
        ),
    ]
