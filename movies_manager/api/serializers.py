from rest_framework import serializers

import sys
sys.path.append("..")
from movies_dash.models import Movies, Film, Hall, HallFilm


class HallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hall
        fields = ('number', 'attendant', 'id')


class MoviesSerializer(serializers.ModelSerializer):
    hall = HallSerializer(required=False)

    # def get_validation_exclusions(self):
        # exclusions = super(MoviesSerializer, self).get_validation_exclusions()
        # return exclusions + ['hall']

    class Meta:
        model = Movies
        fields = ('name', 'hall', 'id')


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ('name', 'main_actor', 'id')


class HallFilmSerializer(serializers.ModelSerializer):
    hall = HallSerializer(required=False)
    film = FilmSerializer(required=False)

    class Meta:
        model = HallFilm
        fields = ('start_date', 'end_date', 'hall', 'film', 'id')
