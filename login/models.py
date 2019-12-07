from django.db import models
from django.utils import timezone
# Create your models here.

gender = (
    ('male', '男'),
    ('female', '女'),
)
class User(models.Model):
    name = models.CharField(max_length=128)
    user_id = models.CharField(max_length=256, unique=True)
    major = models.CharField(max_length=128)
    college = models.CharField(max_length=128)
    degree = models.CharField(max_length=128)
    grade = models.CharField(max_length=128)
    gender = models.CharField(max_length=32, choices=gender, default="男")
    native_place = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=128)
    c_time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


def gender_display2value(dis):
    for i in range(len(gender)):
        if gender[i][1] == dis:
            return gender[i][0]

class Student(models.Model):
    
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128)
    major = models.CharField(max_length=128)
    college = models.CharField(max_length=128)
    degree = models.CharField(max_length=128)
    grade = models.CharField(max_length=128)
    gender = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["c_time"]
        verbose_name = "学生"
        verbose_name_plural = "学生"