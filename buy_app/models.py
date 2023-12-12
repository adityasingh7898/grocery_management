from django.db import models

# Create your models here.

class buy_model(models.Model):
    buy_id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=50)
    quantity=models.PositiveIntegerField()
    t_price = models.PositiveIntegerField()