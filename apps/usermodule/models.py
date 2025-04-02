from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
