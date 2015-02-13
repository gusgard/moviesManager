from django.db import models


class Hall(models.Model):
    number = models.IntegerField()
    attendant = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.number, self.attendant)

    class Meta:
        ordering = ('number',)


class Movies(models.Model):
    name = models.CharField(max_length=16)
    hall = models.ForeignKey(Hall, related_name='halls')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        ordering = ('name',)


class Film(models.Model):
    name = models.CharField(max_length=16)
    main_actor = models.CharField(max_length=16)

    def __str__(self):
        return "%s %s" % (self.name, self.main_actor)

    class Meta:
        ordering = ('name',)


# dont forget utf8!
class HallFilm(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hall = models.OneToOneField(Hall)
    film = models.OneToOneField(Film)