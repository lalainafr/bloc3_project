from django.db import models
# 
# Product
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    Description = models.TextField(max_length=250, default='', blank=True, null=True)
    # image will vbe uploaded in 'media/uploads/product' - cf MEDIAFILE
         
    def __str__(self) -> str:
        return self.name