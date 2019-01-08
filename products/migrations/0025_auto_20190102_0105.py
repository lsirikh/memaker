# Generated by Django 2.1.2 on 2019-01-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20190102_0017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ('-updated', '-added')},
        ),
        migrations.RemoveField(
            model_name='file',
            name='content',
        ),
        migrations.RemoveField(
            model_name='image',
            name='content',
        ),
        migrations.AddField(
            model_name='content',
            name='file',
            field=models.ManyToManyField(to='products.File'),
        ),
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ManyToManyField(to='products.Image'),
        ),
    ]
