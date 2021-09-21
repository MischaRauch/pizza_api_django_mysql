# Generated by Django 3.0.5 on 2021-09-21 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20210921_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='pizza_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.pizza'),
        ),
        migrations.AlterField(
            model_name='order_line',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.orders'),
        ),
        migrations.AlterField(
            model_name='pizza_toppings',
            name='pizza_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.pizza'),
        ),
    ]
