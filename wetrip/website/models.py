from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Login(models.Model):
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=40)
  email = models.EmailField(max_length=50, unique=True)
  
  def __str__(self):
    return self.username


class User(models.Model):
  login = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  location = models.CharField(max_length=50)
  about = models.TextField()
  profile_pic = models.URLField(default='https://www.reinvestmentpartners.org/wp-content/uploads/2015/12/generic-profile.png')
  groups = models.ManyToManyField('Group', blank=True)
  friends = models.ManyToManyField('self', blank=True)

  def __str__(self):
    return self.first_name + self.last_name


class Group(models.Model):
  group_name = models.CharField(max_length=20)

  def __str__(self):
    return str(self.id) + '_' + str(self.group_name)


class Media(models.Model):
  media_title = models.CharField(max_length=20)
  media_url = models.URLField()
  uploader = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.media_url


class Bookmark(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  notes = models.TextField()
  destination = models.ForeignKey('Destination')

  def __str__(self):
    return str(owner) + str(destination)


class Review(models.Model):
  review_text = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  media = models.ManyToManyField(Media, blank=True)
  destination = models.ForeignKey('Destination')

  def __str__(self):
    return str(self.author) + str(self.id)
  

class Destination(models.Model):
  name = models.CharField(max_length=20)


  parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class DestinationInfo(models.Model):
  dest = models.ForeignKey(Destination, on_delete=models.CASCADE)
  trip = models.ForeignKey('Trip')
  order = models.PositiveIntegerField()  

  def __str__(self):
    return str(self.trip) + '_' + str(self.order)


class Trip(models.Model):
  participants = models.ManyToManyField(User)
  name = models.CharField(max_length=20)
  owner = models.ForeignKey(User, related_name="owner")
  dests = models.ManyToManyField(Destination, through=DestinationInfo, blank=True)

  def __str__(self):
    return str(self.id) + '_' + str(self.name)

