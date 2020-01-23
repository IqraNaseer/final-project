from django.db import models
from django.contrib.auth.models import User

subjects = (("Eng","English"),("Math","Maths"),("Programing","Programming"),("Comp","Computer"))


class Test(models.Model):
    category = models.CharField(max_length=64, choices=subjects,default=None)
    question = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255, default=None)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f' {self.user.username} Profile'

class result_db(models.Model):
    res_user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=100)
    eff = models.CharField(max_length=100)
    
    def __str__(self):
        return f' {self.res_user , self.eff} '
