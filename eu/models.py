from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="teacher@gmail.com")
    password = models.CharField(max_length=200, default="123456789")
    

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    dream = models.CharField(max_length=200)
    clasS = models.CharField(max_length=100, default="3 - Informática")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=200)
    _class = models.CharField(max_length=200)
    shift = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)


class School(models.Model):
    name =  models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    phone =  models.CharField(max_length=13)
    adress = models.CharField(max_length=200)
    number =  models.IntegerField()

class Turmas(models.Model):
    Course = models.CharField(max_length=50)
    discipline = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


