from django.db import models

# Create your models here.

class Cities(models.Model):
    city_name = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.city_name


CATEGORIES = [
    ('art', 'Art'),
    ('spo', 'Sport'),
    ('act', 'Active rest'),
    ('cre', 'Creactivity'),
    ('oth', 'Others')
]


class Hobbies(models.Model):
    hobby_name = models.CharField(max_length=100)
    hobby_category = models.CharField(max_length=3, choices=CATEGORIES)

    def __str__(self):
        return self.hobby_name


USER_SEX = [
    ('m', 'male'),
    ('f', 'female')
]


class Users(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=USER_SEX)
    email = models.EmailField(null=True, unique=True)
    hobby = models.ManyToManyField(Hobbies)
    city = models.ForeignKey(Cities, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} years"


class UserRating(models.Model):
    user = models.ManyToManyField(Users)
    user_rating = models.PositiveIntegerField()
    feedback_about_user = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_rating}'


class Places(models.Model):
    place_name = models.CharField(max_length=100, null=False)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    supported_hobbies = models.ManyToManyField(Hobbies)
    place_address = models.CharField(max_length=100)

    def __str__(self):
        return self.place_name


class Arrangements(models.Model):
    arrangement_number = models.PositiveIntegerField()
    user = models.ManyToManyField(Users)
    place = models.ManyToManyField(Places, blank=True)

    def __str__(self):
        return f'Arrangement No. {self.arrangement_number}'


class PlaceRating(models.Model):
    place_rating = models.PositiveIntegerField()
    place_name = models.ForeignKey(Places, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.place_name} - {self.place_rating}'
