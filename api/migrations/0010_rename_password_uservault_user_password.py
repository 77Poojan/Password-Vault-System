# Generated by Django 3.2.13 on 2022-05-23 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20220524_0138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uservault',
            old_name='password',
            new_name='user_password',
        ),
    ]
