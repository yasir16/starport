# Generated by Django 2.2.1 on 2019-05-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190523_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='comments_n',
        ),
        migrations.RemoveField(
            model_name='course',
            name='favorite_n',
        ),
        migrations.RemoveField(
            model_name='course',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='No description yet', max_length=300, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='course',
            name='star_n',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default='Not provided', max_length=40, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
        migrations.AlterField(
            model_name='course',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created on'),
        ),
    ]