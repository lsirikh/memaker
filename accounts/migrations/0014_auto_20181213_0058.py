# Generated by Django 2.1.2 on 2018-12-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20181213_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='account_image/account_pic_default.png', upload_to='account_image/'),
        ),
    ]
