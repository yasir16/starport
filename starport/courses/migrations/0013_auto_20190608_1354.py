# Generated by Django 2.2.1 on 2019-06-08 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20190608_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='approvalqueue',
            options={'permissions': [('approve_course', 'Can approve a course submitted to the Queue')]},
        ),
    ]