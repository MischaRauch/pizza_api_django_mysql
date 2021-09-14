# Generated by Django 3.0.5 on 2021-09-14 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(default=0)),
                ('order_id', models.IntegerField(default=0)),
                ('order_time', models.DateTimeField(verbose_name='orderedTime')),
                ('order_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_name', models.CharField(max_length=200)),
                ('vegeterian', models.BooleanField(default=0)),
                ('price', models.IntegerField(default=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='order_pizza',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Orders'),
        ),
        migrations.AddField(
            model_name='order_pizza',
            name='pizza_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Pizza'),
        ),
    ]
