from django.db import models

# Create your models here.

class Aadhar(models.Model):
    name = models.CharField(max_length=9300)
    address_aadhar_no = models.CharField(max_length=9300)

    def __str__(self):
        return self.name

