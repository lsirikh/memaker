# Generated by Django 2.1.2 on 2019-02-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_infosave'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.PositiveIntegerField(default=0, verbose_name='전화번호'),
            preserve_default=False,
        ),
    ]
