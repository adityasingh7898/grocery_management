from django.urls import path
from customer_app.views import *
app_name = 'customer_app'
urlpatterns=[
    path(route='customer_register/',view=customer_register_view,name='customer_register'),
    path(route='customer_list/',view=customer_list_view,name='customer_list'),
    path(route='cust_category_list/',view=cust_category_list_view,name="cust_category_list"),
    path(route='pro_item_list/',view=pro_item_list_view,name="pro_item_list"),
    
    # path(route='customer_login/',view=customer_login_view,name='customer_login'),
    path(route='customer_logout/',view=customer_logout_view,name='customer_logout'),
    path(route='admin_logout/',view=admin_logout_view,name='admin_logout'),
    path(route='customer_home/',view=customer_home_view,name='customer_home'),
    path(route='forgot_pwd/',view=forgot_pwd_view,name='forgot_pwd'),
    path(route='customer_otp/<int:pk>/',view=customer_otp_view,name='customer_otp'),
    path(route='change_pwd/<int:pk>/',view=change_pwd_view,name='change_pwd'),
    path(route='login_demo/',view=login_demo_view,name='login_demo'),
    path(route='contact/',view=contact_view,name='contact'),
    path(route='cust_detail_update/<int:pk>/',view=cust_detail_update_view,name='cust_detail_update'),
    path(route='admin_login/',view=admin_login_view,name='admin_login')
]