# Generated by Django 3.2.8 on 2023-05-14 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20230514_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='distance',
        ),
        migrations.RemoveField(
            model_name='order',
            name='duration',
        ),
    ]
