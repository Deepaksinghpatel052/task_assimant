from django.db import models
from django.urls import reverse
from datetime import date
import django
# Create your models here.

def user_directory_path(instance, filename):
    producer_id_in_list = instance.ProductName.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format("product/"+producer_id_in_string+"/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)


class product(models.Model):
    ProductName = models.CharField(max_length=120, unique=True)
    ProducImage = models.ImageField(upload_to=user_directory_path)
    Price = models.FloatField(default=0)
    Stock = models.IntegerField(default=0)
    Activate = models.BooleanField(default=True)


    def __str__(self):
        return str(self.ProductName)

    def get_absolute_url(self):
        return reverse('home:ViewProduct')


class webpage(models.Model):
    CompanyName = models.CharField(max_length=120, unique=True)
    CompanyURL = models.URLField(null=True, blank=True)
    Created_date = models.DateField()

    def __str__(self):
        return str(self.CompanyName)