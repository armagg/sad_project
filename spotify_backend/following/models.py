from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from accounts.models import Listener, Singer
from playlists.models import Playlist
from django.db import models

class FollowSinger(models.Model):
    user = ForeignKey(Listener, on_delete=CASCADE)
    singer = ForeignKey(Singer, on_delete=CASCADE)

class FollowPlaylist(models.Model):
    user = models.ForeignKey(Listener, on_delete=CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=CASCADE)
    