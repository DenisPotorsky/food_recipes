from django.db import models


# class User(models.Model):
#     login = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     registration_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.login} {self.password} {self.registration_date}'

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField()
    author = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.description} {self.cooking_steps} {self.cooking_time}'
