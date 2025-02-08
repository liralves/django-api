from django.db import models

class User(models.Model):
    userID = models.CharField(max_length=100, primary_key=True, default='')
    userName = models.CharField(max_length=150, default='')
    userEmail = models.EmailField(default='')
    userAge = models.IntegerField(default=0)

    def __str__(self):
        return f'ID: {self.userID} | Email: {self.userEmail}'


class UserTask(models.Model):
    userID = models.CharField(max_length=100, default='')
    userTask = models.CharField(max_length=255, default='')
