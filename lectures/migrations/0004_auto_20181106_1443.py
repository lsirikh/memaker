# Generated by Django 2.1.2 on 2018-11-06 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_auto_20181106_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
