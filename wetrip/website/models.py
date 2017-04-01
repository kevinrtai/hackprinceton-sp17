from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Login(models.Model):
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=40)


class User(models.Model):
  login = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True)
  email = models.EmailField(max_length=20)
  name = models.CharField(max_length=20)
  profile_pic = models.URLField()
  groups = models.ManyToManyField('Group')
  friends = models.ForeignKey('self', on_delete=models.CASCADE)


class Group(models.Model):
  group_name = models.CharField(max_length=20)


class Media(models.Model):
  media_url = models.URLField()
  uploader = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(models.Model):
  review_text = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  media = models.ManyToManyField(Media)
  destination = models.ForeignKey('Destination')
  

class Destination(models.Model):
  name = models.CharField(max_length=20)
  parent = models.ForeignKey('self', on_delete=models.CASCADE)
  nation = models.BooleanField()
  city = models.BooleanField()
  attraction = models.BooleanField()
  trips = models.ForeignKey


class Trip(models.Model):
  participants = models.ManyToManyField(User)
  name = models.CharField(max_length=20)
  owner = models.ForeignKey(User, related_name="owner")
  dests = models.ManyToManyField(Destination)

