from django.urls import path
from buy_app.views import buy_register,buy_view

app_name='buy_app'
urlpatterns=[
    path(route='buy_register/<int:',view=buy_register,name="buy_register"),
    path(route='buy_view/',view=buy_view,name='buy_view')
]