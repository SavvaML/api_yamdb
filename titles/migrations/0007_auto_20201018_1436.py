# Generated by Django 2.2.9 on 2020-10-18 11:36

import django.core.validators
from django.db import migrations, models
import titles.models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0006_auto_20201014_1505'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='titles',
            options={},
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Название произведения'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.PositiveIntegerField(db_index=True, default=2020, validators=[django.core.validators.MinValueValidator(1450), titles.models.max_value_current_year], verbose_name='Дата публикации произведения'),
        ),
    ]
