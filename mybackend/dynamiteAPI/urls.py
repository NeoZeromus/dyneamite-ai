from django.urls import path
from .views import hello_world
from .views import echo

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('echo/', echo, name='hello_world'),
]
