# Generated by Django 3.2.13 on 2022-05-23 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_userinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='django_password', max_length=256),
        ),
    ]
