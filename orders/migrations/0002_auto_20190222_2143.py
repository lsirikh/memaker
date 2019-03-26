# Generated by Django 2.1.2 on 2019-02-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='address1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(default='', max_length=250, verbose_name='상세주소'),
            preserve_default=False,
        ),
    ]