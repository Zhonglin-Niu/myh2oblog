# Generated by Django 4.0.1 on 2022-01-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='cover',
            field=models.URLField(default='http://pic.myh2o.top/defaultCover', max_length=300, verbose_name='封面图链接'),
        ),
    ]
