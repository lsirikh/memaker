# Generated by Django 2.1.2 on 2018-10-26 14:27

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181026_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_thumbnail',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='product_image/thumbnails', verbose_name='Thumbnails'),
        ),
    ]
