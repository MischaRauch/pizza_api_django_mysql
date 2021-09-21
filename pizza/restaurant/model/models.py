from django.db import models #similar to SQLalchemy 
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)    
    pizza_name = models.CharField(max_length=100) 

    def __str__(self): #function: looking up pizzas         
        return self.pizza_name        

    def __repr__(self): 
        return f"Pizza {self.pizza_id}, {self.pizza_name}"  
        #f: fortmat the return so that it retuns the variable        
         
class topping(models.Model):
    topping_id = models.AutoField(primary_key=True)    
    topping_name = models.CharField(max_length=100)
    topping_price = models.FloatField() 
    vegeterian = models.BooleanField()

    def __str__(self): 
        return self.topping_id

class pizza_toppings(models.Model):
    pizza_toppings_id = models.AutoField(primary_key=True)
    pizza_id = models.ForeignKey(pizza, on_delete=models.CASCADE)    #FK 
    topping_id = models.ForeignKey(topping, on_delete=models.CASCADE)   #FK  
    
    def __str__(self): 
        return self.pizza_toppings_id

class drink(models.Model):
    drink_id = models.AutoField(primary_key=True)    
    drink_name = models.CharField(max_length=100)
    drink_price = models.FloatField() 
    
    def __str__(self): 
        return self.drink_id

class desert(models.Model):
    desert_id = models.AutoField(primary_key=True)    
    desert_name = models.CharField(max_length=100)
    desert_price = models.FloatField() 
    def __str__(self): 
        return self.desert_id

class address(models.Model):
    address_id = models.AutoField(primary_key=True)    
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.IntegerField(default=0) 
    city = models.CharField(max_length=100)
    def __str__(self): 
        return self.address_id

class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=0) 
    discount_available = models.BooleanField(default=False)
    address_id = models.ForeignKey(address, on_delete= models.CASCADE) #FK
    def __str__(self): 
        return self.customer_id

class employee(models.Model):
    employee_id = models.AutoField(primary_key=True)    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    area_code = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.employee_id

class delivery(models.Model):
    Preparation = 'On preparation'
    On_the_way = 'On the way'
    Delivered = 'delivered'
    status_choices = ( 
        (Preparation, 'On preparation'),
        (On_the_way, 'On the way'),
        (Delivered, 'delivered')
    )
    delivery_id = models.AutoField(primary_key=True)    
    employee_id = models.ForeignKey(employee, on_delete=models.CASCADE)    #FK 
    status = models.CharField(max_length=50, choices = status_choices)
    time_when_employee_left = models.DateTimeField('orderedTime')
    
    def __str__(self): 
        return self.delivery_id

class orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)    #FK 
    total_price = models.FloatField(default=0) #calculated from drink, desert and pizza 
    total_discount= models.FloatField(default=0) # get boolean from costumer 
    order_time = models.DateTimeField('orderedTime')
    delivery_id = models.ForeignKey(delivery, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id

class order_item(models.Model):
    order_item_id = models.AutoField(primary_key=True)    
    quantity = models.IntegerField(default=0) 
    pizza_id = models.ForeignKey(pizza, on_delete=models.CASCADE)    #FK
    drink_id = models.ForeignKey(drink, on_delete=models.CASCADE)    #FK 
    desert_id = models.ForeignKey(desert, on_delete=models.CASCADE)    #FK
    order_id = models.ForeignKey(orders, on_delete=models.CASCADE)    #FK
    def __str__(self): 
        return self.order_item_id







    