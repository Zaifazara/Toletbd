# Generated by Django 4.2.6 on 2023-11-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_upazila'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='dividion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
