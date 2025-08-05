from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    def __str__(self):
        return self.username
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)
    gpa = models.FloatField()
