from django.shortcuts import render,redirect
from cart.models import cart_model
from admin_app.models import product_item

from django.contrib import messages

# Create your views here.

def cart_register(request,p_id,cust_id):
    print(p_id,cust_id)
    cart_model.objects.create(cust_id=cust_id,item_id=p_id)
    messages.success(request,"Product is added")
    return redirect('/admin_app/p_list')

def cart_view(request):
    res = cart_model.objects.filter(cust_id=request.user.id)
    prod_data=product_item.objects.all()
    return render(request=request,template_name='cart_list.html',context={'res':res,'prod_data':prod_data})

def cart_remove(request,cart_id):
    cart_model.objects.filter(cart_id=cart_id).delete()
    messages.success(request,"Product is removed")
    return redirect('/cart/cart_list')
