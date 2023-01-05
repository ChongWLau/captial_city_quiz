from django.db import models

# Create your models here.
class Quiz(models.Model):
    
    country = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
