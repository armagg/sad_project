from accounts.models import Listener, Person, Singer
from django.contrib.admin import site

site.register(Person)
site.register(Listener)
site.register(Singer)
