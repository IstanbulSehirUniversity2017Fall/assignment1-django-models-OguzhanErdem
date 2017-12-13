from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.DecimalField
    name = models.CharField(max_length=50)
    description =models.TextField()
    enter_time= models.DateField()

    def __str__(self):
        return self.name
    def __int__(self):
        return self.student_id
class Teacher(models.Model):
    teacher_id = models.DecimalField
    name = models.CharField(max_length=50)
    description =models.TextField()
    enter_time= models.DateField()
    having_students=models.ForeignKey(Student)
    def __str__(self):
        return self.name
    def __int__(self):
        return self.teacher_id