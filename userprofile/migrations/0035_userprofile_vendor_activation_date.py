# Generated by Django 4.2.1 on 2023-06-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0034_userprofile_last_vendor_set_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='vendor_activation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
