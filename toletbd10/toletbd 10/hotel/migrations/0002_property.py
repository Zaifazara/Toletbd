# Generated by Django 4.2.6 on 2023-11-15 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radiocheck', models.CharField(choices=[('family', 'family'), ('sublet', 'sublet'), ('bachelor', 'bachelor'), ('hostel', 'hostel'), ('office', 'office'), ('shop', 'shop')], max_length=10)),
                ('property_title', models.CharField(max_length=60)),
                ('floor_number', models.CharField(max_length=60)),
                ('flat_size', models.CharField(max_length=60)),
                ('price', models.CharField(max_length=10)),
                ('service_charge', models.CharField(max_length=60)),
                ('offer_for', models.CharField(choices=[('Rent', 'Rent'), ('Sale', 'Sale')], max_length=10)),
                ('property_type', models.CharField(choices=[('Owner', 'Owner'), ('Apartment', 'Apartment')], max_length=10)),
                ('building_age', models.CharField(choices=[('0 to 10', '0 to 10'), ('11 to 20', '11 to 20'), ('20 up', '20 up')], max_length=10)),
                ('bed', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10)),
                ('wash', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10)),
                ('balcony', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=10)),
                ('gas', models.CharField(choices=[('LPG', 'LPG'), ('Supply Gas', 'Supply Gas')], max_length=10)),
                ('electricity', models.CharField(choices=[('Prepaid', 'Prepaid'), ('Postpaid', 'Postpaid')], max_length=10)),
                ('security', models.BooleanField(null=True)),
                ('cctv', models.BooleanField(null=True)),
                ('lift', models.BooleanField(null=True)),
                ('parking', models.BooleanField(null=True)),
                ('fire', models.BooleanField(null=True)),
                ('generator', models.BooleanField(null=True)),
                ('address', models.CharField(max_length=250)),
                ('image', models.ImageField(default='no-image.png', upload_to='property/')),
                ('desc', models.TextField(max_length=60)),
                ('family_member', models.CharField(blank=True, max_length=20, null=True)),
                ('sublet_member', models.CharField(blank=True, max_length=20, null=True)),
                ('bachelor_seats', models.CharField(blank=True, max_length=20, null=True)),
                ('hostel_seats', models.CharField(blank=True, max_length=20, null=True)),
                ('hostel_quality', models.CharField(blank=True, max_length=20, null=True)),
                ('hostel_plan', models.FileField(blank=True, null=True, upload_to='floor_plan')),
                ('office_seats', models.CharField(blank=True, max_length=20, null=True)),
                ('shop_quality', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.district')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.division')),
                ('upazila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.upazila')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
