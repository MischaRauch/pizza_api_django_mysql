# Generated by Django 3.2.7 on 2021-10-01 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20211001_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='time_when_employee_left',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='orderedTime'),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='orderedTime'),
        ),
    ]
