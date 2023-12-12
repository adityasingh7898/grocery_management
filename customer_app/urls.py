from django.urls import path
from customer_app.views import customer_register_view,customer_list_view,customer_login_view,customer_home_view,customer_logout_view

app_name = 'customer_app'
urlpatterns=[
    path(route='customer_register/',view=customer_register_view,name='customer_register'),
    path(route='customer_list/',view=customer_list_view,name='customer_list'),
    path(route='customer_login/',view=customer_login_view,name='customer_login'),
    path(route='customer_logout/',view=customer_logout_view,name='customer_logout'),
    path(route='customer_home/',view=customer_home_view,name='customer_home'),
]