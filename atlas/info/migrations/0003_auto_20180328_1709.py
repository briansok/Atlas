# Generated by Django 2.0.3 on 2018-03-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20180328_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='created_at',
        ),
        migrations.AddField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='update',
            name='created_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
