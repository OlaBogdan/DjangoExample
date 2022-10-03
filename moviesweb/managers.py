from django.db import models


class MovieQuerySet(models.QuerySet):
    def after2020(self):
        return self.filter(year__gte=2020)

    def before2020(self):
        return self.filter(year__lt=2020)


class MovieManager(models.Manager):
    def get_queryset(self):
        return MovieQuerySet(self.model, using=self._db)

    def after2020(self):
        return self.get_queryset().after2020()

    def before2020(self):
        return self.get_queryset().before2020()


class MoviesAfter2020Manager(models.Manager):
    def get_queryset(self):
        return super(MoviesAfter2020Manager, self).get_queryset().filter(year__gte=2020)


class MoviesBefore2020Manager(models.Manager):
    def get_queryset(self):
        return super(MoviesBefore2020Manager, self).get_queryset().filter(year__lt=2020)
