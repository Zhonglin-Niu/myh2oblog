# Generated by Django 4.0.1 on 2022-01-28 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userinfo_nick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='nick',
        ),
    ]
