from django.urls import path
from . import movieviews as views

app_name = 'movie_collection'

urlpatterns = [
    path('', views.display_movie_collection, name='video_list'),
    path('movie/<int:pk>/', views.show_movie_details, name='video_detail'),
    path('movie/add/', views.add_new_movie, name='video_create'),
    path('movie/<int:pk>/edit/', views.edit_movie_information, name='video_update'),
    path('movie/<int:pk>/remove/', views.remove_movie_from_collection, name='video_delete'),
]
