from django.db import models

# Create your models here.

class Laptop(models.Model):
    lid = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=40)
    model_name = models.CharField(max_length=40)
    ram = models.IntegerField()
    rom = models.IntegerField()
    processor = models.CharField(max_length=40)
    price = models.FloatField()
    weight = models.FloatField()


    def __str__(self):
        return self.price