from email.policy import default
from unicodedata import decimal
from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
GENDER__CHOICES = [
    ("Male","Male"),
    ("Female","Female"),
]

SPESIFICATION__CHOICES = [
    ("Frontend","Frontend"),
    ("Backend","Backend"),
    ("Mobile/Android","Mobile/Android"),
    ("Mobile/Ios","Mobile/Ios"),
    ("Mobile/Flutter","Mobile/Flutter"),
]

ROOM__CHOICES = [
    ("Room-1","Room-1"),
    ("Room-2","Room-2"),
    ("Room-3","Room-3"),
    ("Room-4","Room-4"),
    ("Room-5","Room-5"),
    ("Room-Extra","Room-Extra"),
]

TIME__CHOICES = [
    ("11:00 - 13:00","11:00 - 13:00"),
    ("13:00 - 15:00","13:00 - 15:00"),
    ("15:00 - 17:00","15:00 - 17:00"),
    ("17:00 - 19:00","17:00 - 19:00"),
    ]

class Mentor(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6,choices=GENDER__CHOICES,default="Male")
    birth_day = models.DateField()
    spesification = models.CharField(max_length=15,choices=SPESIFICATION__CHOICES,default="Frontend") 

    def __str__(self):
        return self.first_name + " " + self.last_name


class Group(models.Model):
    title = models.CharField(max_length=30)
    spesification = models.CharField(max_length=15,choices=SPESIFICATION__CHOICES,default="Frontend")
    mentor = models.OneToOneField(Mentor,on_delete=models.SET_NULL,null=True)
    lesson_qty = models.IntegerField()
    student_qty = models.IntegerField()
    price = MoneyField(max_digits=3, decimal_places=0, default_currency='USD')
    time = models.CharField(max_length=14,choices=TIME__CHOICES,default="11:00 - 13:00")
    room  = models.CharField(max_length=11,choices=ROOM__CHOICES,default="Room-Extra")
    def total_incom(self):
        return self.price * self.student_qty

    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6,choices=GENDER__CHOICES,default="Male")
    birth_day = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    




