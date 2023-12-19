from django.shortcuts import render,redirect
from django.http import HttpResponse
from admin_app.models import category_items,product_item
from customer_app.forms import customer_register_form,customer_login_form,change_pwd_form,customer_update_form
from django.contrib.auth import authenticate,login,logout
from customer_app.models import customer_model
from django.contrib.auth.decorators import login_required
import random
from django.core.mail import send_mail 
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.

def customer_register_view(request):
    form = customer_register_form()
    if request.method=='POST':
        form = customer_register_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful.")
            return redirect('/customer_app/customer_login')
        else:
            messages.error(request,"Not Registered.")
    return render(request=request,template_name='customer_register.html',context={'form':form})


def login_demo_view(request):
    form=customer_login_form()
    if request.method=='POST':
        form=customer_login_form(request.POST)
        if form.is_valid():
            user=authenticate(
                username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect('/customer_app/customer_home')
    return render(request=request,template_name='login_demo.html',context={'form':form})

def customer_list_view(request):
    data = customer_model.objects.all()
    return render(request=request,template_name='customer_list.html',context={'data':data})

def cust_category_list_view(request):
    res=category_items.objects.all()
    return render(request=request,template_name='cust_category_list.html',context={'data':res})
# product list
def pro_item_list_view(request):
    res=product_item.objects.all()
    return render(request=request,template_name='cust_pro_list.html',context={'data':res})

@login_required(login_url='/customer_app/login_demo')
def customer_home_view(request):
    res=category_items.objects.all()
    print(res)
    return render(request=request,template_name='customer_home.html',context={'res':res})

@login_required(login_url='/customer_app/login_demo')
def customer_logout_view(request):
    logout(request)
    return redirect('/customer_app/login_demo')

def forgot_pwd_view(request):
    res=customer_model.objects.all().values_list('email')
    global otp_confirm
    if request.method =='POST':
        otp=random.randint(000000,999999)
        otp_confirm=otp
        email=request.POST['email']
        if (email,) in res:
            subject = 'Customer verification code'
            msg=f'''Dear customer,
                    Please enter the OTP{otp}
                    Thankyou'''
            send_mail(subject=subject,message=msg,from_email=settings.EMAIL_HOST_USER,recipient_list=[email])
            email_id=customer_model.objects.get(email=email)
            return redirect(f'/customer_app/customer_otp/{email_id.id}/')
        else:
            messages.error(request,"Email or OTP is incorrect.")
    return render(request=request,template_name='forgot_pwd.html')

def customer_otp_view(request,pk):
    if request.method=='POST':
        if str(otp_confirm)==str(request.POST['otp']):
            return redirect(f'/customer_app/change_pwd/{pk}/')
        else:
            return redirect('/customer_app/forgot_pwd')
    return render(request=request,template_name='customer_otp.html')

def change_pwd_view(request,pk):
    form = change_pwd_form()
    if request.method=='POST':
        res = customer_model.objects.get(id=pk)
        form=change_pwd_form(request.POST)
        if form.is_valid():
            if form.cleaned_data['enter_new_password']==form.cleaned_data['re_enter_password']:
                customer_model.objects.filter(id=pk).update(password=make_password(form.cleaned_data['enter_new_password']))
                return redirect('/customer_app/login_demo')
    return render(request=request,template_name='create_pwd.html',context={'form':form})


def contact_view(request):
    return render(request=request,template_name='contact.html')

def cust_detail_update_view(request,pk):
    res=customer_model.objects.get(id=pk)
    form=customer_update_form(instance=res)
    if request.method=='POST':
        res=customer_model.objects.get(id=pk)
        form=customer_update_form(request.POST,instance=res)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated")
        else:
            messages.error(request,"Profile is not updated")
        return redirect('/customer_app/customer_home')
    return render(request=request,template_name="cust_detail_update.html",context={'form':form})