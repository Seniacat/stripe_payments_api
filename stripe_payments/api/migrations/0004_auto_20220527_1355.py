# Generated by Django 3.2.13 on 2022-05-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_order_amount_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(default='eur', max_length=3, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='currency',
            field=models.CharField(default='eur', max_length=3, verbose_name='Валюта'),
        ),
    ]
