from django.db import connections
from django.db import models



# Create your models here.

# class Book(models.Model):   
#     BC = models.CharField(max_length=100,primary_key=True)
#     Y2012 = models.IntegerField(max_length=100)
#     Y2013 = models.IntegerField(max_length=100)
#     Y2014 = models.IntegerField(max_length=100)
#     Y2015 = models.IntegerField(max_length=100)
#     Y2016 = models.IntegerField(max_length=100)
#     Y2017 = models.IntegerField(max_length=100)
#     Y2018 = models.IntegerField(max_length=100)
#     Y2019 = models.IntegerField(max_length=100)
#     Y2020 = models.IntegerField(max_length=100)
#     class Meta:
#         db_table = "Book"
class credit(models.Model):
    bc = models.CharField(max_length=100, primary_key=True )
    year = models.IntegerField(max_length=100)
    creditTax = models.CharField(max_length=100)
    bl = models.CharField(max_length=100)
    class Meta:
        db_table = "credit"

class qre(models.Model):
    bc = models.CharField(max_length=100, primary_key=True )
    year = models.IntegerField(max_length=100)
    qreTax = models.CharField(max_length=100)
    bl = models.CharField(max_length=100)
    class Meta:
        db_table = "qre"


class project_list(models.Model):
    year = models.IntegerField(max_length=100)
    bc = models.CharField(max_length=100, primary_key=True )
    project_number = models.IntegerField(max_length=100)
    project_name = models.CharField(max_length=100)
    pm = models.CharField(max_length=100)
    sample_project = models.CharField(max_length=100)
    class Meta:
        db_table = "project_list"
