from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING
from accounts.models import Provider, Singer


POD = 'podcast'
MUSIC = 'music'

MUSIC_TYPE = [
    (POD, 'podcast'),
    (MUSIC, 'music')
]
class Music(models.Model):
    singers = models.ManyToManyField(Singer)
    name = models.CharField(max_length=30)
    file_id = models.IntegerField()
    provider = models.ForeignKey(Provider, on_delete=DO_NOTHING)
    file_type = models.CharField(max_length=7, choices=MUSIC_TYPE)
    lenght = models.IntegerField('time in seconds')
    release_date = models.DateField()
    cover = models.ImageField('cover')
    played_count = models.IntegerField(default=0)

class Genre(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField()

class MusicGenre(models.Model):
    music = models.ForeignKey(Music, CASCADE)
    genre = models.ForeignKey(Genre, CASCADE)
    weight = models.SmallIntegerField()
