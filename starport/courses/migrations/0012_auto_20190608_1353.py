# Generated by Django 2.2.1 on 2019-06-08 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_approvalqueue_submitted_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='approvalqueue',
            options={'permissions': [('approve_course', 'Can approve a course submitted to the Queue'), ('remove_course', 'Can remove a course from the Queue')]},
        ),
    ]