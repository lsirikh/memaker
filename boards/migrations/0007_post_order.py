# Generated by Django 2.1.2 on 2018-12-21 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_auto_20181221_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
