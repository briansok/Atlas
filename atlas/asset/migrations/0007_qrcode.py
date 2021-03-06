# Generated by Django 2.0.3 on 2018-03-28 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0006_hardware_ssd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
        ),
    ]
