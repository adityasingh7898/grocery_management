from django.shortcuts import render,redirect
from buy_app.models import buy_model,buyed_item_list
from django.contrib import messages
from admin_app.models import product_item
from cart.models import cart_model
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/customer_app/login_demo')
def buy_register(request,total_price):
    if request.method=='POST':
        print('hai')
        print(request.POST)
        buy=buy_model.objects.create(cust_id=request.user.id,total_price=total_price,cust_name=request.POST['cust_name'],
                                    cust_phone=request.POST['cust_phone'],
                                    cust_address=request.POST['cust_address'])
        res=cart_model.objects.filter(cust_id=request.user.id).values()
        print(res)
        for i in res:
            #store the item in buyed model
            buyed_item_list.objects.create(buy_id=buy.buy_id,item_id=i['item_id'],item_name=i['item_name'],item_price=i['price'],quantity=i['quantity'])
            # quantity update
            quantity=product_item.objects.get(item_id=i['item_id']).item_quantity
            print(quantity)
            product_item.objects.filter(item_id=i['item_id']).update(item_quantity=(quantity-1))
            #items delete in cart
            cart_model.objects.filter(cust_id=request.user.id).delete()
        messages.success(request,"Order is placed")
        return redirect('/buy_app/order_details')
    return render(request=request,template_name='buy_confirm.html')

@login_required(login_url='/customer_app/login_demo')
def buy_view(request):
    prod_data=cart_model.objects.all()
    total_price=cart_model.objects.filter(cust_id=request.user.id).aggregate(Sum('price'))
    print(prod_data)
    return render(request=request,template_name='buy_list.html',context={'prod_data':prod_data,'total_price':total_price})
@login_required(login_url='/customer_app/login_demo')
def order_details(request):
    cust_details=buy_model.objects.filter(cust_id=request.user.id)
    items_details=buyed_item_list.objects.all()
    return render(request=request,template_name='order_details.html',context={'cust_details':cust_details,'items_details':items_details})

@login_required(login_url='/customer_app/login_demo')
def order_list(request):
    cust_details=buy_model.objects.all()
    items_details=buyed_item_list.objects.all()
    return render(request=request,template_name='order_details.html',context={'cust_details':cust_details,'items_details':items_details})