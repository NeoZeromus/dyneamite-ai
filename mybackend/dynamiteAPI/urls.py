from django.urls import path
from .views import hello_world
from .views import echo, create_post

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('echo/', echo, name='hello_world'),
    path('create_post/', create_post, name='create_post'),
]
