# Generated by Django 4.2.1 on 2023-05-29 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_userprofile_is_user_alter_userprofile_is_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_user',
        ),
    ]
