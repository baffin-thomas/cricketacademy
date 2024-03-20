from django.db import models
class cricket(models.Model):
    Date=models.CharField(max_length=100)
    TeamName=models.CharField(max_length=100)
    TotalPLayers=models.IntegerField()
    place=models.CharField(max_length=100)
    Hours=models.IntegerField()
    Fees=models.IntegerField()

# Create your models here.