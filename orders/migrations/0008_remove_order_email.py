# Generated by Django 2.1.2 on 2019-02-23 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_totalcost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
    ]
