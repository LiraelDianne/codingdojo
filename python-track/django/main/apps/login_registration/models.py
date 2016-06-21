from __future__ import unicode_literals

from django.db import models
import re, bcrypt

NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
EMAIL_REGEX = re.compile(r'^[\w\.\+-]+@[\w\.-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def login(self, email, password):
        errors = {}
        user = self.get(email__iexact=email)
        if user:
            if bcrypt.hashpw(password.encode('utf-8'), user[0].password.encode('utf-8')) == user[0].password:
                return (user[0], True)
            else:
                errors['login-password'] = "Password incorrect"
        else:
            errors['login-email'] = "Email not in database"
        return (errors, False)


    def register(self, **kwargs):
        first_name = kwargs['first_name'][0]
        last_name = kwargs['last_name'][0]
        email = kwargs['email'][0]
        password = kwargs['password'][0]
        confirm_password = kwargs['password_confirm'][0]

        errors = {}
        if len(first_name) > 1:
            if not NAME_REGEX.match(first_name):
                errors['first_name'] = "First name must be letters only"
        else:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(last_name) > 1:
            if not NAME_REGEX.match(last_name):
                errors['last_name'] = "Last name must be letters only"
        else:
            errors['last_name'] = "Last name must be at least 2 characters"
        if len(email) > 0:
            if not EMAIL_REGEX.match(email):
                errors['email'] = "Email is not valid"
        else:
            errors['email'] = "Email must not be empty"
        if password == confirm_password:
            if len(password) < 8:
                errors['password'] = "Password must be at least 8 characters"
        else:
            errors['password'] = "Password confirmation does not match"
        if errors:
            return (errors, False)

        encrypted_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': encrypted_pass
        }
        return (user, True)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
    objects = models.Manager()
