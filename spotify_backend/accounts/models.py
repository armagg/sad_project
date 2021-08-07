from django.db import models
from django.contrib.auth import models as auth
from django.db.models.deletion import CASCADE



FREE = 'FREE'
VIP = 'VIP'
ACC_TYPES = [
    (FREE, 'free'),
    (VIP, 'vip')
]

class Person(models.Model):
    user = models.OneToOneField(auth.User, on_delete=CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class Listener(models.Model):
    user = models.ForeignKey(Person, on_delete=CASCADE)
    account_type = models.CharField(choices=ACC_TYPES, max_length=5)

    def __str__(self) -> str:
        return str(self.user)


class Singer(models.Model):
    name = models.CharField(max_length=16, default='خواننده')
    description = models.TextField('descriptions')
    biography = models.TextField()

    def __str__(self) -> str:
        return self.name


class Provider(models.Model):
    user = models.ForeignKey(Person, on_delete=CASCADE)
    balance = models.IntegerField()
    

    def __str__(self) -> str:
        return str(self.user)