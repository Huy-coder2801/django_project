# Generated by Django 3.2.8 on 2023-05-14 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20230514_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='lng',
        ),
    ]
