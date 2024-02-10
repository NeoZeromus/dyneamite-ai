from django.urls import path
from .views import hello_world
from .views import echo, create_post, create_API_object

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('echo/', echo, name='hello_world'),
    path('create_post/', create_post, name='create_post'),
    path('create_API_object/', create_API_object, name='create_API_object')
]
