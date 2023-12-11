from django.shortcuts import render,redirect
from admin_app.models import product_category,category_item
from django.http import HttpResponse

# Create your views here.

#   ============ CATEGORY Register, List, Update, Delete
def category_register_view(request):
    if request.method=='POST':
        category_item.objects.create(cat_name=request.POST['cat_name'])
        return redirect('/admin_app/category_list')
    return render(request=request,template_name='category_register.html')

def category_list_view(request):
    res=product_category.objects.all()
    return render(request=request,template_name='category_list.html',context={'data':res})

def category_update_view(request,pk):
    res=product_category.objects.get(cat_id=pk)
    if request.method=="POST":
        print(request.POST)
        product_category.objects.filter(cat_id=pk).update(cat_name=request.POST['name'])
        return redirect('/admin_app/category_list')
    return render(request=request,template_name='category_update.html',context={'data':res})

def category_delete_view(request,pk):
    res=product_category.objects.get(cat_id=pk)
    if request.method=='POST':
        res=product_category.objects.get(cat_id=pk).delete()
        return redirect('/admin_app/category_list')
    return render(request=request,template_name='category_delete.html',context={'data':res})


#   ============ (item) PRODUCT Register, List, Update, Delete
def item_register_view(request):
    if request.method=='POST':
        print(request)
        print(request.POST)
        print(request.POST['name'],request.POST['email'])
        category_item.objects.create(item_id=request.POST['item_id'],
                                item_name=request.POST['item_name'],
                                item_desc=request.POST['item_desc'],
                                item_quantity=request.POST['item_quantity'],
                                price=request.POST['price'],)
        return redirect('/category_item/list')

    return render(request=request,template_name='item_register.html') 

def item_list_view(request):
    res=category_item.objects.all()
    return render(request=request,template_name='item_list.html',context={'data':res})


def item_update_view(request,pk):
    if request.method=="POST":
        print(request.POST)
        category_item.objecs.filter(cat_id=pk).update(item_name=request.POST['item_name'],
        item_desc=request.POST['item_desc'],item_quantity=request.POST['item_quantity'],price=request.POST['price'])
        return redirect('/cat_items/list')
    res=category_item.objects.get(cat_id=pk_list)
    return render(request=request,template_name='update.html',context={'data':res})


def item_delete_view(request,pk):
    res=category_item.object.get(cat_id=pk)
    if request.method=='POST':
        res=category_item.objects.get(cat_id=pk).delete()
        return redirect('/admin_app/list')
    return render(request=request,template_name='item_delete.html',context={'data':res})
