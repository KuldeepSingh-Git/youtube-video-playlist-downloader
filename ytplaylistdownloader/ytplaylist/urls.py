from django.urls import path 
from . import views

urlpatterns = [
    path('', views.base, name = 'base'),
    path('playlist_link.html/', views.playlist, name = 'download_playlist'),
    path('video_link.html/', views.video, name = 'download_video'),
]