# Generated by Django 2.1.2 on 2019-03-13 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20190313_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
    ]
