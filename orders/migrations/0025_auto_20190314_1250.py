# Generated by Django 2.1.2 on 2019-03-14 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_order_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCancel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, default='', max_length=250, null=True, verbose_name='사유')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='취소일자')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='confirm',
            field=models.CharField(choices=[('001', '미정'), ('002', '확정'), ('003', '취소')], default='001', max_length=4, verbose_name='구매결정'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='주문일자'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderItem', to='orders.Order'),
        ),
        migrations.AddField(
            model_name='ordercancel',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='orderCancel', to='orders.Order'),
        ),
    ]
