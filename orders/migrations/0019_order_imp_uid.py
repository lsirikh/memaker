# Generated by Django 2.1.2 on 2019-03-11 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_order_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='imp_uid',
            field=models.CharField(blank=True, default=0, max_length=500, null=True, verbose_name='아임포트'),
        ),
    ]