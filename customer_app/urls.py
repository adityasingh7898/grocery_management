from django.urls import path
from customer_app.views import customer_register_view,customer_list_view,customer_login_view

app_name = 'customer_app'
urlpatterns=[
    path(route='c_register/',view=customer_register_view,name='customer_register'),
    path(route='c_list/',view=customer_list_view,name='customer_list'),
    path(route='c_login/',view=customer_login_view,name='customer_login'),
]