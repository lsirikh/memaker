# Generated by Django 2.1.2 on 2018-12-13 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20181213_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='route',
            field=models.CharField(blank=True, choices=[('BLG', '네이버블로그'), ('SRC', '인터넷검색'), ('NWS', '뉴스 및 기사'), ('FBK', '페이스북'), ('ING', '인스타그램'), ('REC', '지인소개'), ('EDU', '강의교육'), ('ETC', '기타')], max_length=5, null=True),
        ),
    ]
