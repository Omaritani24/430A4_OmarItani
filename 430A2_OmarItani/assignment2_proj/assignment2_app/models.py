from django.db import models

class Video(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length=100)
    actor1_name = models.CharField(max_length=100)
    actor2_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    movie_genre = models.CharField(max_length=100)
    release_year = models.IntegerField()

    def __str__(self):
        return self.movie_title

    class Meta:
        ordering = ['movie_title']
