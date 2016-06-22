from __future__ import unicode_literals

from django.db import models

from ..login_registration.models import User


class Message(models.Model):
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    user_profile = models.ForeignKey(User, related_name='profile_messages')


class Comment(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    message = models.ForeignKey(Message)
