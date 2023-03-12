from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    type_user = models.CharField(max_length=20)

# Create your models here.
class Student(models.Model):
    name_student = models.CharField(max_length=150)
    name_college = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    # year_adm = models.IntegerField()
    year_pass = models.IntegerField()
    mobile = models.BigIntegerField()


class Teacher(models.Model):
    name_teacher = models.CharField(max_length=150)
    name_college = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    age = models.IntegerField()


class College(models.Model):
    name_college = models.CharField(max_length=200)
    no_department = models.IntegerField()
    clg_code = models.IntegerField()
    address = models.CharField(max_length=200)
    no_teachers = models.IntegerField()
    no_students = models.IntegerField()
