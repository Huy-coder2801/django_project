# Generated by Django 3.2.8 on 2023-05-11 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_category_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pickup_adress',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='pickup_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='pickup_lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='pickup_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='pickup_phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
