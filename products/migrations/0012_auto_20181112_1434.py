# Generated by Django 2.1.2 on 2018-11-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_detail_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='lower_line',
            field=models.BooleanField(default=False, verbose_name='upper line'),
        ),
        migrations.AddField(
            model_name='detail',
            name='upper_line',
            field=models.BooleanField(default=False, verbose_name='upper line'),
        ),
    ]
