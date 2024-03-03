from django.db import models

# Create your models here.

class UserFormData(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122,unique=True)
    mobile = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=122)
    qualification = models.CharField(max_length=122)
    batch = models.CharField(max_length=122)
    college = models.CharField(max_length=250)
    city = models.CharField(max_length=122)


    def __str__(self):
        return str(self.name)
