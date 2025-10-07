from django import forms
from django.core.exceptions import ValidationError
from .models import Video

class MovieEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom styling and placeholders
        self.fields['movie_title'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter the movie title...',
            'style': 'border-radius: 15px; border: 2px solid #e9ecef;'
        })
        self.fields['actor1_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Lead actor name',
            'style': 'border-radius: 10px; border: 2px solid #e9ecef;'
        })
        self.fields['actor2_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Supporting actor name',
            'style': 'border-radius: 10px; border: 2px solid #e9ecef;'
        })
        self.fields['director_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Director name',
            'style': 'border-radius: 10px; border: 2px solid #e9ecef;'
        })
        self.fields['movie_genre'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'e.g., Action, Drama, Comedy',
            'style': 'border-radius: 10px; border: 2px solid #e9ecef;'
        })
        self.fields['release_year'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'e.g., 2023',
            'min': '1900',
            'max': '2030',
            'style': 'border-radius: 10px; border: 2px solid #e9ecef;'
        })

    def clean_release_year(self):
        year = self.cleaned_data.get('release_year')
        if year and (year < 1900 or year > 2030):
            raise ValidationError('Release year must be between 1900 and 2030.')
        return year

    def clean_movie_title(self):
        title = self.cleaned_data.get('movie_title')
        if title and len(title.strip()) < 2:
            raise ValidationError('Movie title must be at least 2 characters long.')
        return title.strip()

    class Meta:
        model = Video
        fields = ['movie_title', 'actor1_name', 'actor2_name', 'director_name', 'movie_genre', 'release_year']
        labels = {
            'movie_title': 'Film Title',
            'actor1_name': 'Lead Actor',
            'actor2_name': 'Supporting Actor',
            'director_name': 'Director',
            'movie_genre': 'Genre',
            'release_year': 'Year Released',
        }
        help_texts = {
            'movie_title': 'Enter the full title of the movie',
            'actor1_name': 'Name of the main actor',
            'actor2_name': 'Name of the supporting actor',
            'director_name': 'Name of the film director',
            'movie_genre': 'Category or type of movie',
            'release_year': 'Year the movie was released',
        }
