from django.db import models


# Create your models here.

class cart_model(models.Model):
    cart_id=models.AutoField(primary_key=True)
    cust_id=models.PositiveIntegerField()
    item_id=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField(default=1)