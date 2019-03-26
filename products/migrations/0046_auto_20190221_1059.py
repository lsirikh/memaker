# Generated by Django 2.1.2 on 2019-02-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0045_merge_20190120_1745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
    ]