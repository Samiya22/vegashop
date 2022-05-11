from tabnanny import verbose
from django.db import models


class Post(models.Model):

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"



    name = models.CharField(max_length=50)  
    price = models.IntegerField()
    info = models.TextField()
    
    def __str__(self):
        return self.name
