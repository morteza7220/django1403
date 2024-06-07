from django.db import models
import json
    
class options(models.Model):
    # id=models.IntegerField()
    op1=models.CharField(max_length=255)
    op2=models.CharField(max_length=255)
    op3=models.CharField(max_length=255)
    op4=models.CharField(max_length=255)
    answer=models.CharField(max_length=255)
    
# Create your models here.
class Question(models.Model):
    # id=models.IntegerField()
    text=models.CharField(max_length=255)
    # tiles=models.Model.JSONField(blank=True)
    options=models.ForeignKey(options,default=None, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

