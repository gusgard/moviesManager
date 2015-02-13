from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
import sys
sys.path.append("..")
# import movies_manager.movies_dash
# from ..movies_dash.models import *
from movies_dash.models import Hall, Movies, Film, HallFilm
from serializers import HallSerializer, MoviesSerializer, FilmSerializer, HallFilmSerializer

# Hall class based views


class HallMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Hall.objects.all()
    serializer_class = HallSerializer


class HallList(HallMixin, ListCreateAPIView):
    """
    Return a list of all the halls, or
    create new ones
    """
    pass


class HallDetail(HallMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific hall, update it, or delete it.
    """
    pass

# Movies class based views


class MoviesMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class MoviesList(MoviesMixin, ListCreateAPIView):
    """
    Return a list of all the movies, or
    create new ones
    """
    pass


class MoviesDetail(MoviesMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific movies, update it, or delete it.
    """
    pass

# Film class based views


class FilmMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmList(FilmMixin, ListCreateAPIView):
    """
    Return a list of all the films, or
    create new ones
    """
    pass


class FilmDetail(FilmMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific film, update it, or delete it.
    """
    pass

# HallFilm class based views


class HallFilmMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = HallFilm.objects.all()
    serializer_class = HallFilmSerializer


class HallFilmList(HallFilmMixin, ListCreateAPIView):
    """
    Return a list of all the hallfilms, or
    create new ones
    """
    pass


class HallFilmDetail(HallFilmMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific hallfilm, update it, or delete it.
    """
    pass
