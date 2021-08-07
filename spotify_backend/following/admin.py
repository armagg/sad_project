
from following.models import FollowPerson, FollowPlaylist, FollowSinger
from django.contrib.admin import site

site.register([FollowPlaylist, FollowSinger, FollowPerson])

