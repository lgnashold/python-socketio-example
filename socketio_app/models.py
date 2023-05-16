from django.db import models

# Create your models here.


class MyModel(models.Model):
    my_field = models.CharField(max_length = 128)
