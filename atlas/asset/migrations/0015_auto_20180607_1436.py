# Generated by Django 2.0.3 on 2018-06-07 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asset', '0014_auto_20180413_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.TextField(blank=True, null=True)),
                ('license_amount', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name_plural': 'License',
                'verbose_name': 'License',
            },
        ),
        migrations.RemoveField(
            model_name='asset',
            name='user',
        ),
        migrations.RemoveField(
            model_name='software',
            name='license',
        ),
        migrations.RemoveField(
            model_name='software',
            name='license_amount',
        ),
        migrations.AddField(
            model_name='hardware',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='license',
            name='software',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Software'),
        ),
        migrations.AddField(
            model_name='license',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
