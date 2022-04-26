from django.db import models

class Lead(models.Model):
    ismi = models.CharField(max_length=20)
    familyasi = models.CharField(max_length=20)
    yoshi = models.IntegerField(default=16)
    

