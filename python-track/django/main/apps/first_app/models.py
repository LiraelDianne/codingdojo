from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def login(self, email, password):
        #login logic here
    def register(self, **kwargs):
        #register logic here

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()


class Message(models.Model):
    message = models.TextField()
    user_id = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message_id = ForeignKey(Message)
    user_id = ForeignKey(User)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
