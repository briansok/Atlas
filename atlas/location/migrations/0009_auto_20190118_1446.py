# Generated by Django 2.0.10 on 2019-01-18 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0008_auto_20180613_1815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['title'], 'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
    ]
