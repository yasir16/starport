# Generated by Django 2.2.2 on 2019-06-20 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20190608_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='approvalqueue',
            options={'ordering': ['-submitted_on', 'submitted_by'], 'permissions': [('approve_course', 'Can approve a course submitted to the Queue by setting status as True'), ('remove_course', 'Can remove a course from the Queue by setting status as False')]},
        ),
    ]