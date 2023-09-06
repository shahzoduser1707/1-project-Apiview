from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_date = models.DateTimeField('date published')



class Choice(models.Model):
    question = models.ForeignKey(Product,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,default='iltimos tanlang')
    votes = models.IntegerField(default=1)

class Branch(models.Model):
    branch_id = models.SmallIntegerField
    branch_date = models.DateTimeField('date published')

class Workers(models.Model):
    workers_count = models.SmallIntegerField
    workers_date_of_birth = models.DateTimeField('date published')

class Director(models.Model):
    director_name = models.CharField(max_length=200)
