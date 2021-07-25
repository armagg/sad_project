from django.db import models
from django.contrib.auth import models as auth
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField


FREE = 'FREE'
VIP = 'VIP'
ACC_TYPES = [
    (FREE, 'free'),
    (VIP, 'vip')
]

class User(auth.User):
    pass


class Listener(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    account_type = models.CharField(choices=ACC_TYPES, max_length=5)


class Singer(models.Model):
    name = models.CharField(max_length=16, default='خواننده')
    description = models.TextField('descriptions')
    biography = models.TextField()


class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    balance = models.IntegerField()