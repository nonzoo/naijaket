# Generated by Django 4.2.1 on 2023-05-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='WhatsApp_No',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
