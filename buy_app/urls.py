from django.urls import path
from buy_app.views import buy_register,buy_view,order_details,order_list
app_name='buy_app'

urlpatterns=[
    path(route='buy_register/<int:total_price>/',view=buy_register,name="buy_register"),
    path(route='buy_view/',view=buy_view,name='buy_view'),
    path(route='order_details/',view=order_details,name='order_details'),
    path(route='order_list/',view=order_list,name='order_list'),
]