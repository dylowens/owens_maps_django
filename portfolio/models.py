# Create your models here.
from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='works/')
    
    def __str__(self):
        return self.title
