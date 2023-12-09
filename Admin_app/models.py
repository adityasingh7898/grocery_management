from django.db import models

# Create your models here.
class product_category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=50)

class category_item(models.Model):
    cat_id=models.ForeignKey(product_category, on_delete=models.CASCADE)
    item_id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=50)
    item_desc=models.TextField()
    item_quantity=models.PositiveIntegerField()
    price=models.FloatField()