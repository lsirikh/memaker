# Generated by Django 2.1.2 on 2018-12-12 15:05

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_email_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='img/account_pic_default.png', upload_to=accounts.models.user_directory_path),
        ),
    ]
