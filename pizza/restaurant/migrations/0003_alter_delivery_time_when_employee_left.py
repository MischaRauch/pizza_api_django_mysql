# Generated by Django 3.2.7 on 2021-09-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_delivery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='time_when_employee_left',
            field=models.DateTimeField(auto_now_add=True, verbose_name='orderedTime'),
        ),
    ]