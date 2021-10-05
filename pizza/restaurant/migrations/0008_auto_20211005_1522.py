# Generated by Django 3.0.5 on 2021-10-05 13:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20211001_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='time_when_employee_left',
        ),
        migrations.AddField(
            model_name='employee',
            name='status_employee',
            field=models.CharField(default='Free', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='discount_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 5, 13, 22, 36, 16692, tzinfo=utc), verbose_name='orderedTime'),
        ),
    ]
