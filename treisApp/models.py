from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.rollno

