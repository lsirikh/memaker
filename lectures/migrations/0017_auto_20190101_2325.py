# Generated by Django 2.1.2 on 2019-01-01 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20190101_2325'),
        ('lectures', '0016_auto_20190101_2325'),
        ('products', '0020_auto_20190101_2325'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Lecture',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
