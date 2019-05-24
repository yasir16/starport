# Generated by Django 2.2.1 on 2019-05-23 13:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190523_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvalqueue',
            name='repo_url',
            field=models.URLField(unique=True, validators=[django.core.validators.URLValidator], verbose_name='repo url'),
        ),
    ]