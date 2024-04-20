from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
  is_visitor = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)
  email = models.EmailField(unique=True)
  photo = models.ImageField(upload_to='ProfilePhoto')

  EMAIL_FIELD = 'email'
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destination_images/')

    def __str__(self):
        return self.name


class BookATour(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.destination}"


class Package(models.Model):

    package_pic = models.ImageField(upload_to='package_images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    days = models.PositiveIntegerField()
    person = models.PositiveIntegerField()
    

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username
