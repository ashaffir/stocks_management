# Generated by Django 3.0.2 on 2020-01-19 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kadima', '0002_stockdata_stam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdata',
            name='stam',
        ),
    ]