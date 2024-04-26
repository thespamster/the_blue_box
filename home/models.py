from django.db import models

# Create your models here.

class Doctors(models.Model):   
    name = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'Doctors'
   
    def __str__(self):
        return self.name