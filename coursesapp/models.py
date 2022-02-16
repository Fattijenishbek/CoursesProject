from enum import Enum
from tkinter import CASCADE
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    imgpath = models.TextField()

    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude=models.TextField()
    longtitude=models.TextField()
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.address

class Contact(models.Model):
    # class STATUS(Enum):
    #     first=(1, ('PHONE')),
    #     second=(2,('FACEBOOK')),
    #     third=(3,('EMAIL'))

    #     @classmethod
    #     def get_value(cls, choice):
    #         return cls.value[0]

    # type = models.IntegerField(
    #     choices=[x.value for x in STATUS],
    #     default=STATUS.get_value(STATUS.first[0]),
    # )
    type=models.IntegerField()
    value=models.CharField(max_length=100)


class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    logo=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    contacts=models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='courses')
    branches=models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='courses')


