from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.CharField(max_length=20, unique=True)
    department=models.CharField(max_length=100)
    semester=models.IntegerField()
    gpa=models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name} ({self.rollno})"