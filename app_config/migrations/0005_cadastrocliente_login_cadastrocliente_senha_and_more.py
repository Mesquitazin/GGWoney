# Generated by Django 4.2.6 on 2023-11-03 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_config', '0004_remove_cadastrocliente_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrocliente',
            name='login',
            field=models.CharField(default='0', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='cadastrocliente',
            name='senha',
            field=models.CharField(default='0', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='cpf',
            field=models.CharField(max_length=15),
        ),
    ]