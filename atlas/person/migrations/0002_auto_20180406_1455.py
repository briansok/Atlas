# Generated by Django 2.0.3 on 2018-04-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrator'), ('user', 'User')], default='user', max_length=7),
        ),
    ]
