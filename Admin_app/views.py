from django.shortcuts import render,redirect
from admin_app.models import category_items,product_item
from admin_app.forms import product_form
from django.contrib import messages
from customer_app.models import customer_model
from django.contrib.auth.decorators import login_required

# Create your views here.

#   ============ CATEGORY Register, List, Update, Delete
@login_required(login_url='/customer_app/admin_login')
def category_register_view(request):
    if (request.user.is_staff or request.user.is_superuser) and request.method=='POST':
        if category_items.objects.create(cat_name=request.POST['cat_name']):
            messages.success(request,"Category is added.")
        else:
            messages.error(request,"Category is not added.")
        return redirect('/admin_app/category_list')
    return render(request=request,template_name='category_register.html')

@login_required(login_url='/customer_app/admin_login')
def category_list_view(request):
    if (request.user.is_staff or request.user.is_superuser):
        res=category_items.objects.all()
        return render(request=request,template_name='category_list.html',context={'data':res})

@login_required(login_url='/customer_app/admin_login')
def category_update_view(request,pk):
    res=category_items.objects.get(cat_id=pk)
    if (request.user.is_staff or request.user.is_superuser) and request.method=="POST":
        print(request.POST)
        if category_items.objects.filter(cat_id=pk).update(cat_name=request.POST['name']):
            messages.success(request,"Category Updated")
        else:
            messages.error(request,"Category is not Updated")
        return redirect('/admin_app/category_list')
    return render(request=request,template_name='category_update.html',context={'data':res})

@login_required(login_url='/customer_app/admin_login')
def category_delete_view(request,pk):
    res=category_items.objects.get(cat_id=pk)
    if (request.user.is_staff or request.user.is_superuser) and request.method=='POST':
        if category_items.objects.get(cat_id=pk).delete():
            messages.success(request,"Category Deleted")
        else:
            messages.error(request,"Category is not Deleted")
        return redirect('/admin_app/category_list')
    return render(request=request,template_name='category_delete.html',context={'data':res})


@login_required(login_url='/customer_app/admin_login')
def cust_prod_list_view(request):
    if (request.user.is_staff or request.user.is_superuser):
        res=category_items.objects.all()
        return render(request=request,template_name='cust_prod_list.html',context={'data':res})


#   ============ (item) PRODUCT Register, List, Update, Delete

@login_required(login_url='/customer_app/admin_login')
def item_register_view(request):
    form=product_form()
    if (request.user.is_staff or request.user.is_superuser) and request.method=='POST' and request.FILES:
        form=product_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Product added")
        else:
            messages.error(request,"Product is not added")
        return redirect('/admin_app/p_list/')
    return render(request=request,template_name='item_register.html',context={'form':form}) 


@login_required(login_url='/customer_app/admin_login')
def item_list_view(request):
    if (request.user.is_staff or request.user.is_superuser):
        res=product_item.objects.all()
        return render(request=request,template_name='item_list.html',context={'data':res})


@login_required(login_url='/customer_app/admin_login')
def item_details_view(request):
    if request.method=='POST':
        res=product_item.objects.filter(cat_id=request.POST['cat_list'])
        return render(request=request,template_name='cust_prod_list.html',context={'data':res})
    return render(request=request,template_name='item_list.html',context={'data':res})


@login_required(login_url='/customer_app/admin_login')
def item_update_view(request,pk):
    res=product_item.objects.get(item_id=pk)
    form=product_form(instance=res)
    if (request.user.is_staff or request.user.is_superuser) and request.method=="POST":
        res=product_item.objects.get(item_id=pk)
        form=product_form(request.POST,request.FILES, instance=res)
        if form.is_valid():
            form.save()
            messages.success(request,"Product Updated")
        else:
            messages.error(request,"Product is not Updated")
        return redirect('/admin_app/p_list')
    return render(request=request,template_name='item_update.html',context={'form':form})

@login_required(login_url='/customer_app/admin_login')
def item_delete_view(request,pk):
    res=product_item.objects.get(item_id=pk)
    if (request.user.is_staff or request.user.is_superuser) and request.method=='POST':
        if product_item.objects.get(item_id=pk).delete():
            messages.success(request,"Product Deleted")
        else:
            messages.error(request,"Product is not deleted")
        return redirect('/admin_app/p_list')
    return render(request=request,template_name='item_delete.html',context={'data':res})

@login_required(login_url='/customer_app/admin_login')
def customer_list_view(request):
    data = customer_model.objects.all()
    return render(request=request,template_name='customers.html',context={'data':data})