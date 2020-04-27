from django.shortcuts import render
from django.http import HttpResponse

def schedule(request):
    return HttpResponse('Well, this is the schedule for movies')


def description(request):
    return HttpResponse('Well, this is the description for a movie')


def intro(request):
    return render(request, 'movies/movies.html')


def first_movie(request):
    data = {'title': 'The Good, The Bad and The Ugly',
             'synopsis': 'A western movie',
             'release': '1996'}
    return render(request, 'movies/first_movie.html', data)


def get_all_movies(request):
    data = {'movies': [
            {'title': 'The God, The Bad & The Ugly',
            'synopsis': 'A western movie',
            'release': '1996'},
            {'title': 'The God, The Bad & The Ugly',
            'synopsis': 'A western movie',
            'release': '1996'},
            {'title': 'The God, The Bad & The Ugly',
            'synopsis': 'A western movie',
            'release': '1996'},]
    }
    return render(request, 'movies/all-movies.html', data)

def get_all_movies(request):
    movies = Movie.objects.all()
    data = {'movies': movies}

    return render(request, 'movies/all-movies.html', data)

