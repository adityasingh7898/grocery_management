from django.db import models

# Create your models here.
class category_items(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=50)
    def __str__(self):
        return self.cat_name

class product_item(models.Model):
    cat_id=models.ForeignKey(category_items, on_delete=models.CASCADE)
    item_id=models.AutoField(primary_key=True)
    item_name=models.CharField(max_length=50)
    item_desc=models.TextField()
    item_quantity=models.PositiveIntegerField()
    price=models.FloatField()
    img=models.ImageField(upload_to='items/')
    def __str__(self):
        return self.item_name