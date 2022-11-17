# Generated by Django 4.1.3 on 2022-11-17 22:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, validators=[django.core.validators.RegexValidator(inverse_match=True, message='Регистрация с указанного домена запрещена!', regex='@rambler.ru')], verbose_name='email address'),
        ),
    ]
