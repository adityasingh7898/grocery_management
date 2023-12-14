from django.urls import path
from admin_app.views import category_register_view, category_list_view, category_update_view, category_delete_view, item_register_view, item_list_view, item_update_view, item_delete_view,item_details_view
app_name='admin_app'
urlpatterns = [
    path(route='category_register/',view=category_register_view,name="category_register"),
    path(route='category_list/',view=category_list_view,name="category_list"),
    path(route='category_update/<int:pk>/',view=category_update_view,name="category_update"),
    path(route='category_delete/<int:pk>/',view=category_delete_view,name="category_delete"),

    # ----PRODUCT----
    path(route='p_register/',view=item_register_view,name="p_register"),
    path(route='p_list/',view=item_list_view,name="p_list"),
    path(route='p_details/',view=item_details_view,name="p_details"),
    path(route='p_update/<int:pk>/',view=item_update_view,name="p_update"),
    path(route='p_delete/<int:pk>/',view=item_delete_view,name="p_delete"),
]