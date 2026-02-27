import datetime

from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(upload_to='students/',null=True,blank=True)
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(default='Male', max_length=20)
    date = models.CharField(default=datetime.date.today)

    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=20)
    exam_code = models.CharField(max_length=30)
    date = models.DateField()

    def __str__(self):
        return self.name