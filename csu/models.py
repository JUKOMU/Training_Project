from django.db import models


# Create your models here.
class User(models.Model):
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=30)


class PasswordRule(models.Model):
    rule = models.CharField(max_length=10)
