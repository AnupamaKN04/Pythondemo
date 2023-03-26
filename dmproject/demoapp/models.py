from django.db import models

# Create your models here.
class Name(models.Model):

    img=models.ImageField(upload_to='pics')
    name = models.CharField(max_length=250)
    desc=models.TextField()