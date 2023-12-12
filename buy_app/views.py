from django.shortcuts import render,redirect
from buy_app.models import buy_model
from django.contrib import messages
from cart.models import cart_model
from admin_app.models import product_item

# Create your views here.

def buy_register(request,p_name,p_,price):
    print(p_name,price)
    buy_model.objects.create(item_name=p_name,t_price=price)
    messages.success(request,"Product is added")
    return redirect('/admin_app/p_list')

def buy_view(request):
    res=product_item.objects.all()
    prod_data=cart_model.objects.all().values()
    print(prod_data)
    return render(request=request,template_name='buy_list.html',context={'res':res,'prod_data':prod_data})
