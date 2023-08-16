from django.db import models

# Create your models here.
class Product(models.Model):
    p_name = models.CharField(max_length=200)
    p_catagory = models.CharField(max_length=100)
    p_disc = models.TextField()
    p_price = models.FloatField()
    p_img =  models.ImageField(upload_to='images/', blank=True, null=True)
    