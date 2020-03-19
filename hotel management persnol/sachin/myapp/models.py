from django.db import models
import uuid
class Room(models.Model):

    no = models.IntegerField()
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to="image")


class Reserve(models.Model):

    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    contactno = models.IntegerField()
    email = models.EmailField()
    nofc = models.IntegerField()
    nofa = models.IntegerField

