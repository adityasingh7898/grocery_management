from django.db import models
from django.contrib.auth.models import User
from admin_app.models import product_item,category_items

# Create your models here.

class customer_model(User):

    phone = models.PositiveBigIntegerField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10,choices=[['Male','Male'],['Female','Female'],['other','other']])

class cart_model(models.Model):
    cat_id=models.ForeignKey(category_items, on_delete=models.CASCADE)
    item_id=models.ForeignKey(product_item, on_delete=models.CASCADE)
    item_name=models.ForeignKey(product_item, on_delete=models.CASCADE)
    price=models.ForeignKey(product_item, on_delete=models.CASCADE)
