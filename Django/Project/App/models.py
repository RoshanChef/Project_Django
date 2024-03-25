from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=25 , default = "1")
    def __str__(self):
        return self.name

class author(models.Model):
    name = models.CharField(max_length=20)
    post = models.ImageField(upload_to="Images/")


class feedback(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField()