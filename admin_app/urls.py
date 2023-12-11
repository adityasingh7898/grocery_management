from django.urls import path
from admin_app.views import category_register_view, category_list_view, category_update_view, category_delete_view, item_register_view, item_list_view, item_update_view, item_delete_view

app_name='admin_app'
urlpatterns = [
    path(route='',view=category_register_view,name="category_register"),
    path(route='category_list/',view=category_list_view,name="category_list"),
    path(route='category_update/<int:pk>/',view=category_update_view,name="category_update"),
    path(route='category_delete/<int:pk>/',view=category_delete_view,name="category_delete"),

    # ----PRODUCT----
    path(route='p_register',view=item_register_view,name="register"),
    path(route='p_list/',view=item_list_view,name="list"),
    path(route='p_update/<int:pk>/',view=item_update_view,name="item_update"),
    path(route='p_delete/<int:pk>/',view=item_update_view,name="item_delete"),
]