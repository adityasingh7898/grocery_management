from django.contrib import admin
from admin_app.models import product_item,category_items

# Register your models here.
class category(admin.ModelAdmin):
    list_display=['cat_id','cat_name']
admin.site.register(category_items,category)

class items(admin.ModelAdmin):
    product_display=['item_id','item_name','item_desc','item_quantity','price']
admin.site.register(product_item,items)