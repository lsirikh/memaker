# Generated by Django 2.1.2 on 2019-03-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20190223_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='전화번호'),
        ),
    ]
