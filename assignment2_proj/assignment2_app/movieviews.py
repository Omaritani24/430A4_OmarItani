from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Video
from .movieforms import MovieEntryForm

def display_movie_collection(request):
    """Display all movies in the collection"""
    movies = Video.objects.all().order_by('-movie_id')
    return render(request, 'assignment2_app/movie_collection.html', {'videos': movies})

def show_movie_details(request, pk):
    """Display detailed information about a specific movie"""
    movie = get_object_or_404(Video, pk=pk)
    context = {
        'video': movie,
        'related_movies': Video.objects.filter(
            Q(movie_genre=movie.movie_genre) | Q(director_name=movie.director_name)
        ).exclude(pk=pk)[:3]
    }
    return render(request, 'assignment2_app/movie_details.html', context)

def add_new_movie(request):
    """Add a new movie to the collection"""
    if request.method == 'POST':
        form = MovieEntryForm(request.POST)
        if form.is_valid():
            movie = form.save()
            messages.success(request, f'Movie "{movie.movie_title}" has been added to your collection!')
            return redirect('movie_collection:video_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MovieEntryForm()
    
    return render(request, 'assignment2_app/delete.html', {
        'form': form, 
        'title': 'Add New Movie',
        'action': 'create'
    })

def edit_movie_information(request, pk):
    """Edit existing movie information"""
    movie = get_object_or_404(Video, pk=pk)
    
    if request.method == 'POST':
        form = MovieEntryForm(request.POST, instance=movie)
        if form.is_valid():
            updated_movie = form.save()
            messages.success(request, f'Movie "{updated_movie.movie_title}" has been updated successfully!')
            return redirect('movie_collection:video_detail', pk=movie.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MovieEntryForm(instance=movie)
    
    return render(request, 'assignment2_app/delete.html', {
        'form': form, 
        'title': f'Edit {movie.movie_title}',
        'action': 'update',
        'movie': movie
    })

def remove_movie_from_collection(request, pk):
    """Remove a movie from the collection"""
    movie = get_object_or_404(Video, pk=pk)
    
    if request.method == 'POST':
        movie_title = movie.movie_title
        movie.delete()
        messages.success(request, f'Movie "{movie_title}" has been removed from your collection.')
        return redirect('movie_collection:video_list')
    
    return render(request, 'assignment2_app/video_confirm_delete.html', {'video': movie})
