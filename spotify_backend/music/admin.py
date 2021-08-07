from music.models import Genre, Music, MusicGenre
from django.contrib.admin import site

site.register(Music)
site.register(MusicGenre)
site.register(Genre)
