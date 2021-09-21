# Generated by Django 3.0.5 on 2021-09-21 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('postal_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(default=0)),
                ('discount_available', models.BooleanField(default=False)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.address')),
            ],
        ),
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('On preparation', 'On preparation'), ('On the way', 'On the way'), ('delivered', 'delivered')], max_length=50)),
                ('time_when_employee_left', models.DateTimeField(verbose_name='orderedTime')),
            ],
        ),
        migrations.CreateModel(
            name='desert',
            fields=[
                ('desert_id', models.AutoField(primary_key=True, serialize=False)),
                ('desert_name', models.CharField(max_length=100)),
                ('desert_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='drink',
            fields=[
                ('drink_id', models.AutoField(primary_key=True, serialize=False)),
                ('drink_name', models.CharField(max_length=100)),
                ('drink_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('area_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('pizza_id', models.AutoField(primary_key=True, serialize=False)),
                ('pizza_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='topping',
            fields=[
                ('topping_id', models.AutoField(primary_key=True, serialize=False)),
                ('topping_name', models.CharField(max_length=100)),
                ('topping_price', models.FloatField()),
                ('vegeterian', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='pizza_toppings',
            fields=[
                ('pizza_toppings_id', models.AutoField(primary_key=True, serialize=False)),
                ('pizza_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.pizza')),
                ('topping_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.topping')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_price', models.FloatField(default=0)),
                ('total_discount', models.FloatField(default=0)),
                ('order_time', models.DateTimeField(verbose_name='orderedTime')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer')),
                ('delivery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.delivery')),
            ],
        ),
        migrations.CreateModel(
            name='order_item',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('desert_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.desert')),
                ('drink_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.drink')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.orders')),
                ('pizza_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.pizza')),
            ],
        ),
        migrations.AddField(
            model_name='delivery',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.employee'),
        ),
    ]