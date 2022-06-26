from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    certified = models.BooleanField(default=False)
    highScore = models.IntegerField(default=0)
    dateAcquired = models.DateField(null=True,blank=True)

    def __str__(self) :
        return self.user.username
        

class Workout(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __str__(self) :
        return self.name

class Split(models.Model):
    name = models.CharField(max_length=200,unique=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class Muscle(models.Model):
    name = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)

    def __str__(self) :
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    splits = models.ManyToManyField(Split)
    description = models.TextField()
    muscle = models.ManyToManyField(Muscle,related_name='muscle_id')
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)

    def __str__(self) :
        return self.name



