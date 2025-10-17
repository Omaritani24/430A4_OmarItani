from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'movie_title', 'director_name', 'movie_genre', 'release_year')
    list_filter = ('movie_genre', 'release_year')
    search_fields = ('movie_title', 'director_name', 'actor1_name', 'actor2_name')
    ordering = ('movie_title',)
