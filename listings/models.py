from django.db import models
from realtors.models import Realtor
from datetime import datetime

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    clubhouse = models.IntegerField()
    sqft = models.IntegerField()
    estate_size = models.FloatField(default=0.0)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.title

    
