from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Login(models.Model):
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=40)
  
  def __str__(self):
    return self.username


class User(models.Model):
  login = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True)
  email = models.EmailField(max_length=50)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  profile_pic = models.URLField(blank=True, null=True)
  groups = models.ManyToManyField('Group', blank=True, null=True)
  friends = models.ManyToManyField('self', blank=True, null=True)

  def __str__(self):
    return self.first_name + self.last_name


class Group(models.Model):
  group_name = models.CharField(max_length=20)

  def __str__(self):
    return self.group_name


class Media(models.Model):
  media_title = models.CharField(max_length=20)
  media_url = models.URLField()
  uploader = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.media_url


class Review(models.Model):
  review_text = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  media = models.ManyToManyField(Media, blank=True, null=True)
  destination = models.ForeignKey('Destination')

  def __str__(self):
    return str(self.author) + str(self.id)
  

class Destination(models.Model):
  name = models.CharField(max_length=20)
  parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Trip(models.Model):
  participants = models.ManyToManyField(User)
  name = models.CharField(max_length=20)
  owner = models.ForeignKey(User, related_name="owner")
  dests = models.ManyToManyField(Destination, blank=True, null=True)

  def __str__(self):
    return self.name

