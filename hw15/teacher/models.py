from django.db import models

class Teacher(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    experience = models.IntegerField()
    profile_photo = models.FileField()

    def __str__(self):
        return self.fname