from django.urls import path
from .views import schedule, description, intro, first_movie, get_all_movies


urlpatterns = [
    path('schedule', schedule, name="schedule"),
    path('description', description),
    path('intro', intro),
    path('first_movie', first_movie),
    path('all_movies', get_all_movies)
]