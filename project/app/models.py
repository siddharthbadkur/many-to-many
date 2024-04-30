from django.db import models

# Create your models here.
fuel=[
    ('diesal','diesal'),
    ('petrol','petrol'),
    ('cng','cng')
]

class  FuelModel(models.Model):
    fuel_name=models.CharField(max_length=100,choices=fuel)
    def __str__(self):
        return self.fuel_name

car=[
    ('maruthi','maruthi'),
    ('toyata','toyata')
 ] 
class Carmodel(models.Model): 
    car_name= models.CharField(max_length=100,choices=car)
    fuel_name= models.ManyToManyField(FuelModel)
    def __str__(self):   
        return self.car_name 
