# Generated by Django 2.0.3 on 2018-03-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_asset_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
