# Generated by Django 3.2.8 on 2023-05-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_driver_earnings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(default=15000.0),
        ),
    ]