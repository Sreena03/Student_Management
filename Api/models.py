from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    registration_number =models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNo = models.CharField(max_length=10)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

