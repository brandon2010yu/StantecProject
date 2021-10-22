
from django.db import connections
from django.db import models

# Create your models here.

class Book(models.Model):   
    BC = models.CharField(max_length=100,primary_key=True)
    Y2012 = models.CharField(max_length=100)
    Y2013 = models.CharField(max_length=100)
    Y2014 = models.CharField(max_length=100)
    Y2015 = models.CharField(max_length=100)
    Y2016 = models.CharField(max_length=100)
    Y2017 = models.CharField(max_length=100)
    Y2018 = models.CharField(max_length=100)
    Y2019 = models.CharField(max_length=100)
    Y2020 = models.CharField(max_length=100)
    class Meta:
        db_table = "Book"
