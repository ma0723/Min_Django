from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie


# Create your views here.
@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_GET
def recommended(request):
    recent_movies = Movie.objects.order_by('-release_date')[:5]
    old_movies = Movie.objects.order_by('release_date')[:5]
    
    context = {
        'recent_movies' : recent_movies,
        'old_movies' : old_movies
    }

    return render(request, 'movies/recommended.html', context)

