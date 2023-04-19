from django.db import models

# Create your models here.
class Users(models.Model):
    USER_SEX = [
        ('m', 'male'),
        ('f', 'female')
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=USER_SEX)
    email = models.EmailField(null=True, unique=True)
    city = models.CharField(max_length=100, default="Minsk")

    def __str__(self):
        return self.name


class Establishments(models.Model):
    places = [
        (1, 'restaurant'),
        (2, 'cafe'),
        (3, 'bar')
    ]
    name = models.CharField(max_length=40)
    category = models.IntegerField(choices=places)
    address = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=40)


    def __str__(self):
        return self.name


