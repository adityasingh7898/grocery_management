from django.shortcuts import render,redirect
from cart.models import cart_model
from admin_app.models import product_item
from django.db.models import Sum,Avg,Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/customer_app/customer_login')
def cart_register(request,p_id,cust_id,iname,iprice):
    print(p_id,cust_id)
    iprice=int(float(iprice))
    res=cart_model.objects.create(cust_id=cust_id,item_id=p_id,item_name=iname,price=iprice)
    print(res.cart_id)
    messages.success(request,"Product is added")
    return redirect('/admin_app/p_list')

@login_required(login_url='/customer_app/customer_login')
def cart_view(request):
    res = cart_model.objects.filter(cust_id=request.user.id)
    prod_data=product_item.objects.all()
    total_price=cart_model.objects.filter(cust_id=request.user.id).aggregate(Sum('price'))
    return render(request=request,template_name='cart_list.html',context={'res':res,'prod_data':prod_data,'total_price':total_price})

@login_required(login_url='/customer_app/customer_login')
def cart_remove(request,cart_id):
    cart_model.objects.filter(cart_id=cart_id).delete()
    messages.success(request,"Product is removed")
    return redirect('/cart/cart_list')
