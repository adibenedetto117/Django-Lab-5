from django.urls import path
from .views import hello_world, hello_world_page

urlpatterns = [
    path('', hello_world),
    path('page/', hello_world_page) 
]