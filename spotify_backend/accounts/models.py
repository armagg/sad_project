from django.db import models
from django.contrib.auth import models as auth
from django.db.models.deletion import CASCADE


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
    user = models.ForeignKey(User, on_delete=CASCADE)
    description = models.TextField('descriptions')
    biography = models.TextField()


