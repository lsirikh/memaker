# Generated by Django 2.1.2 on 2019-01-18 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_auto_20190118_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='content',
            name='slug',
        ),
    ]