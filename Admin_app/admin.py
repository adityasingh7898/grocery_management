from django.contrib import admin
from Admin_app.models import product_category,category_item

# Register your models here.
class category(admin.ModelAdmin):
    list_display=['cat_id','cat_name']
admin.site.register(product_category,category)

class items(admin.ModelAdmin):
    product_display=['item_id','item_name','item_desc','item_quantity','price']
admin.site.register(category_item,items)