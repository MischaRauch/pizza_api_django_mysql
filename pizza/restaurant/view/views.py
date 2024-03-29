from datetime import date
import datetime
import json
import re
from sys import set_asyncgen_hooks
from django.http.response import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from restaurant.controller import queries 
from restaurant.model.models import pizza, drink, desert, orders 
from django.core import serializers


#For testing purposes
def test(request):
    print ('im here          ' )
   # queries.get_delivery_time_and_status_from_order(1)
    queries.get_delivery_time_and_status_from_order(1) 
    return HttpResponse('Success')

#returns all pizzas
def get_all_pizzas(request):
    pizza_list = pizza.objects.order_by('-pizza_id')
    print("RAW DATA: ", pizza_list)
    #print(model_to_dict(pizza_list))
    data = serializers.serialize('json', pizza_list, fields=('pizza_id','pizza_name'))
    return JsonResponse(data, safe= False)
    
#returns one pizza with ingridients and price
def get_one_pizza(request, pizza_id): 
    toppings = queries.get_toppings(pizza_id)
    price = queries.get_pizza_price(pizza_id)
    toppings.append(price)    
    toppings = json.dumps(toppings)
    return JsonResponse(str(toppings), safe= False)

#returns true or false if pizza is vegeterian
def get_vegetarian(request, pizza_id):
    veggi = queries.is_pizza_vegetarian(pizza_id)
    print('VEGGI ',veggi)
    data = json.dumps(veggi)
    return JsonResponse(data, safe=False)

def get_drinks(request):
    drink_list = drink.objects.order_by('-drink_id')
    data = serializers.serialize('json', drink_list, fields=('drink_id','drink_name'))
    return JsonResponse(data, safe= False)

def get_drink_price(request, drink_id):
    price = queries.get_drink_price2(drink_id)
    data = json.dumps(price)
    return JsonResponse(data, safe=False)

def get_deserts(request):
    drink_list = desert.objects.order_by('-desert_id')
    print("LOOKS LIKE ", drink_list)
    data = serializers.serialize('json', drink_list, fields=('desert_id','desert_name'))
    return JsonResponse(data, safe= False)

def get_desert_price(request, desert_id):
    price = queries.get_desert_price2(desert_id)
    print("YUHUHU MISCHA ", price)
    data = json.dumps(price)
    return JsonResponse(data, safe=False)

def get_orders(request):
    status = request.GET.get('status')
    order_list = queries.get_orders_by_delivery_status(status)
    data = serializers.serialize('json', order_list, fields=('order_id', 'order_time'))
    return JsonResponse(data, safe=False)

#shows the ordered items and quantity, the estimated delivery time, status and amount of money
def get_show_order(request):
    global new_order
    print('HELLO order ', new_order)
    stuff = queries.get_show_order(new_order)
    data = json.dumps(stuff)
    return JsonResponse(data, safe=False)

def get_delivery_estimation(request):
    global new_order
    info = queries.get_delivery_time_and_status_from_order(new_order.order_id)
    data = json.dumps(info)
    return JsonResponse(data, safe=False)


@csrf_exempt
def update_order_status(request, order_id):
    new_status = request.POST['new_status']
    queries.update_delivery_status_using_order_id(order_id, new_status)
    return HttpResponse('Success')

#TODO 
@csrf_exempt
def update_employee_status(request):
    queries.update_employee_status()
    return HttpResponse('Success')



#creates a customer
@csrf_exempt
def create_customer(request):
    if (request.method == 'POST'):
        print("DATA" ,request.POST['first_name'])
        #postal_code, country, street, house_number, city, first_name, last_name, email, phone
        global new_order
        new_order = queries.create_new_order_new_customer(request.POST['postal_code'],request.POST['country'],request.POST['street'],request.POST['house_number'],request.POST['city'],request.POST['first_name'], request.POST['last_name'],request.POST['email'],request.POST['phone'])
        if (new_order == False):
             return HttpResponseNotAllowed('All deliveries are busy.')
        print("NEW ORDER ",new_order)  
    return HttpResponse('Success')

@csrf_exempt
def get_customer(request):
    if (request.method == 'POST'):
        global new_order
        print("GOT HERE")
        new_order = queries.create_new_order_old_customer(request.POST['customer_id'])
        print("ORDERRRR ", new_order)
        if (new_order == False):
             return HttpResponseNotAllowed('All deliveries are busy.')
    return HttpResponse('Success')
   

@csrf_exempt
def create_order_item(request):  
    if (request.method == 'POST'):   
        if (((request.POST['drink_id']) == '9999') and ((request.POST['desert_id']) == '9999') ):
            print("ORRDDDERDS ",new_order)
            queries.create_order_item(new_order, request.POST['quantity'], request.POST['pizza_id'])
        if (((request.POST['pizza_id']) == '9999') and ((request.POST['desert_id']) == '9999') ):
          
            queries.create_order_item(new_order, request.POST['quantity'], None, request.POST['drink_id'])
        if (((request.POST['pizza_id']) == '9999') and ((request.POST['drink_id']) == '9999') ):
           
            queries.create_order_item(new_order, request.POST['quantity'], None, None,  request.POST['desert_id'])
        
    else:
        print('NO POST')
    
    return HttpResponse('Success')

@csrf_exempt
def cancel_order(request):
    print("GOTTT HERE 234")
    if (request.method == 'POST'):   
        print("GOTTT HERE")
        queries.delete_order(request.POST['order_id'])
    else:
        print('NO POST')
    return HttpResponse('Success')

@csrf_exempt
def order_info(request):
    if (request.method == 'POST'):
        print("DATAAA ",request.POST['order_id'])
        string = queries.get_delivery_time_and_status_from_order2(request.POST['order_id'])
        data = json.dumps(string)
        print("STIRNG SS", data)
        return JsonResponse(data, safe=False)
    else:
        print("NO POST")
    return HttpResponse('Success')














#def my_custom_sql():
#    cursor = connection.cursor()
#    cursor.execute("SELECT * FROM menu_pizza")
#    row = cursor.fetchall()
#    return row
#
#def query(request):
#    cursor = connection.cursor()
#    cursor.execute("SELECT * FROM menu_pizza WHERE pizza_id = 1")
#    row = cursor.fetchall()
#    print(row)
#    return render(row,'detail.html')
