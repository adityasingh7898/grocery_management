from django.db import models

# Create your models here.

class buy_model(models.Model):
    buy_id=models.AutoField(primary_key=True)
    cust_id=models.PositiveIntegerField()    
    total_price=models.IntegerField()
    cust_name=models.CharField(max_length=50)
    cust_phone=models.PositiveBigIntegerField()
    cust_address=models.TextField()
    order_date=models.DateField(auto_now=True)

class buyed_item_list(models.Model):
    buy_id=models.PositiveBigIntegerField()
    item_id=models.PositiveBigIntegerField()
    item_name=models.CharField(max_length=50)
    item_price=models.FloatField()
    quantity=models.PositiveIntegerField()


