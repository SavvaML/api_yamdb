# Generated by Django 2.2.9 on 2020-09-30 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='book',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='film',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='music',
        ),
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
