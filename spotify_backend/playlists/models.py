from django.db.models.deletion import CASCADE, SET_NULL
from accounts.models import Listener
from django.db import models
from music.models import Music

class Playlist(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField()
    visibility = models.BooleanField(default=True)
    is_liked_songs = models.BooleanField(default=False)
    owner = models.ForeignKey(Listener,related_name='owner', on_delete=SET_NULL, null=True)
    admins = models.ManyToManyField(Listener)

class PlaylistMusic(models.Model):
    playlist = models.ForeignKey(Playlist, db_index=True, on_delete=CASCADE)
    music =  models.ForeignKey(Music, db_index = True, on_delete=CASCADE)
    added_date = models.DateField()
    added_by = models.ForeignKey(Listener, on_delete=SET_NULL, null=True)
