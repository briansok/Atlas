# Generated by Django 2.0.3 on 2018-04-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_location_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='plan',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
