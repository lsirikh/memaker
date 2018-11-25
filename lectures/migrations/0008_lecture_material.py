# Generated by Django 2.1.2 on 2018-11-08 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20181107_1255'),
        ('lectures', '0007_lecture_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='material',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
    ]
