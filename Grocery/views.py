from django.shortcuts import render

def home_view(request):
    return render(request=request,template_name='gms_home.html')