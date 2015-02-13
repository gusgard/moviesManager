from django.contrib import admin
# from django.contrib.gis import admin
from models import Film, Hall, HallFilm, Movies


class HallAdmin(admin.ModelAdmin):
    list_display = ('number', 'attendant')

admin.site.register(Hall, HallAdmin)


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'hall')
admin.site.register(Movies, MoviesAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_actor')
admin.site.register(Film, FilmAdmin)


class HallFilmAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'hall', 'film')
admin.site.register(HallFilm, HallFilmAdmin)