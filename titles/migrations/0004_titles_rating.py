# Generated by Django 2.2.9 on 2020-10-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0003_auto_20201013_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]