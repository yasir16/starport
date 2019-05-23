# Generated by Django 2.2.1 on 2019-05-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courseset_updated_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseset',
            name='favorite_n',
        ),
        migrations.AddField(
            model_name='courseset',
            name='course_n',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='courseset',
            name='description',
            field=models.TextField(default='No description yet', max_length=300, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='courseset',
            name='image',
            field=models.URLField(null=True, verbose_name='repo image'),
        ),
        migrations.AddField(
            model_name='courseset',
            name='star_n',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='courseset',
            name='title',
            field=models.CharField(default='None', max_length=40, verbose_name='title'),
            preserve_default=False,
        ),
    ]
