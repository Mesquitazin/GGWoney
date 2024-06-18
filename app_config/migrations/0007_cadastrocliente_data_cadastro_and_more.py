# Generated by Django 4.2.6 on 2023-11-10 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_config', '0006_alter_cadastrocliente_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrocliente',
            name='data_cadastro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='empresa',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='login',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='senha',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
