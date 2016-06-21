from __future__ import unicode_literals
from django.db import models

from ..login_registration.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User)
