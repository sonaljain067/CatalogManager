from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 250)
    category = models.CharField(max_length = 250)
    brand_name = models.CharField(max_length = 250)
    image = models.FileField(upload_to="product_images")
    
    def __str__(self):
        return self.name
