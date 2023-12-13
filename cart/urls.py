from django.urls import path
from cart.views import cart_view,cart_register,cart_remove

app_name='cart_app'
urlpatterns=[
    path(route='cart_list/',view=cart_view,name='cart_list'),
    path(route='cart_register/<int:p_id>/<int:cust_id>/<str:iname>/<iprice>/',view=cart_register,name='cart_register'),
    path(route='cart_remove/<int:cart_id>/',view=cart_remove,name='cart_remove'),
]