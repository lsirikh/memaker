# Generated by Django 2.1.2 on 2019-01-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20190106_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='replychapter',
            name='is_reply_to_reply',
            field=models.BooleanField(blank=True, default=False, verbose_name='대댓글 여부'),
        ),
        migrations.AddField(
            model_name='replychapter',
            name='reply_to_reply_address',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='대상댓글'),
        ),
    ]
