# Generated by Django 2.1.2 on 2018-11-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0012_auto_20181117_2206'),
        ('products', '0015_remove_product_related_lec'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_lec',
            field=models.ManyToManyField(to='lectures.Lecture'),
        ),
    ]
