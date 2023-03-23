from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()

