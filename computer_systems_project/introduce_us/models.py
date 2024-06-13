from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    bio = models.TextField()
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name

