# Generated by Django 4.2.1 on 2023-09-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_alter_product_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_pt',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
