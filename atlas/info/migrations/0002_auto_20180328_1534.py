# Generated by Django 2.0.3 on 2018-03-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
