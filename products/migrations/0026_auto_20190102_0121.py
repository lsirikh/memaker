# Generated by Django 2.1.2 on 2019-01-01 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20190102_0105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('section',)},
        ),
    ]
