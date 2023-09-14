from django.db import models

# Create your models here.
class Todo(models.Model):
    task_name=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)

class Reminder(models.Model):
    reminder_name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.TextField()
    icon = models.CharField(max_length=20)

    def __str__(self):
        return self.city
    
