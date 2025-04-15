from django.urls import path
from .views import recevoir_position, home

urlpatterns = [
    path('', home, name='home'),
    path('position/', recevoir_position, name='recevoir_position'),
]