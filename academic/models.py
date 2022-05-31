from operator import mod
from django.db import models

# Create your models here.
class Grade(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=50)
    credits = models.PositiveIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.name, self.credits)
    
