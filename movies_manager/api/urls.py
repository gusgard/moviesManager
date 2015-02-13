from django.conf.urls import patterns, url

# Class based API views
from views import HallList, HallDetail, MoviesList, MoviesDetail, FilmList, FilmDetail, HallFilmList, HallFilmDetail

urlpatterns = patterns('',

    # Class based URLs,
    url(r'^halls/$', HallList.as_view(), name='hall_list'),
    url(r'^halls/(?P<pk>[0-9]+)/$', HallDetail.as_view(), name='hall_detail'),

    url(r'^movies/$', MoviesList.as_view(), name='movies_list'),
    url(r'^movies/(?P<pk>[0-9]+)/$', MoviesDetail.as_view(), name='movies_detail'),

    url(r'^films/$', FilmList.as_view(), name='film_list'),
    url(r'^films/(?P<pk>[0-9]+)/$', FilmDetail.as_view(), name='film_detail'),

    url(r'^hallfilms/$', HallFilmList.as_view(), name='hallfilm_list'),
    url(r'^hallfilms/(?P<pk>[0-9]+)/$', HallFilmDetail.as_view(), name='hallfilm_detail'),

    )