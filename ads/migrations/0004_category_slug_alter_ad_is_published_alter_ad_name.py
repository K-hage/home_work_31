# Generated by Django 4.1.3 on 2022-11-17 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=123, max_length=10, validators=[django.core.validators.MinLengthValidator(5)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='is_published',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
