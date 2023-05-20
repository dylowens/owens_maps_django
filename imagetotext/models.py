from django.db import models

# Create your models here.


class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
