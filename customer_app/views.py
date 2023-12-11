from django.shortcuts import render,redirect
from customer_app.forms import customer_register_form,customer_login_form
from django.contrib.auth import authenticate,login,logout
from customer_app.models import customer_model
from django.contrib.auth.decorators import login_required

# Create your views here.

def customer_register_view(request):
    form = customer_register_form()
    if request.method=='POST':
        form = customer_register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer_login')
    return render(request=request,template_name='customer_register.html',context={'form':form})

def customer_login_view(request):
    form=customer_login_form()
    if request.method=='POST':
        form=customer_login_form(request.POST)
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect('/customer_home')
    return render(request=request,template_name='customer_login.html',context={'form':form})

def customer_list_view(request):
    data = customer_model.objects.all()
    return render(request=request,template_name='customer_list.html',context={'data':data})

@login_required(login_url='/customer_app/customer_login')
def customer_home_view(request):
    return render(request=request,template_name='customer_home.html')

@login_required(login_url='/customer_app/customer_login')
def customer_logout_view(request):
    logout(request)
    return redirect('/customer_app/customer_login')
