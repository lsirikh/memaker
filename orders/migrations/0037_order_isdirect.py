# Generated by Django 2.1.2 on 2019-03-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0036_auto_20190319_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='isDirect',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='바로구매'),
        ),
    ]