from django.db import models

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=32)

class Student(models.Model):
    name = models.CharField(max_length=16)
    grade = models.ForeignKey(Grade,on_delete = models.CASCADE)
