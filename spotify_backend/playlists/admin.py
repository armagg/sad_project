from playlists.models import Playlist, PlaylistMusic
from django.contrib.admin import site

site.register([Playlist, PlaylistMusic])