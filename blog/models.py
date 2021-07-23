from django.db import models
from django.utils import timezone
# Create your models here.
class joke(models.Model):
    category = models.CharField(max_length= 1000)
    joke = models.TextField()
    created = models.DateTimeField(auto_now_add=True)