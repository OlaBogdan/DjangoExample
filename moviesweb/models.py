from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext as _

from moviesweb.managers import MoviesAfter2020Manager, MoviesBefore2020Manager, MovieManager
from moviesweb.validators import validate_year


class Movie(models.Model):
    title = models.CharField(max_length=1024, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000, validators=[MaxValueValidator(2022), ])
    description = models.TextField(default='')
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)
    additional_info = models.OneToOneField('AdditionalInfo', related_name='movie', on_delete=models.CASCADE, null=True,
                                           blank=True)

    # movies_after_2022 = MoviesAfter2020Manager()
    # movies_before_2022 = MoviesBefore2020Manager()
    objects = MovieManager()

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return f'{self.title} ({self.year})'

    def save(self, *args, **kwargs):
        validate_year(self.year)

        super(Movie, self).save(*args, **kwargs)


class AdditionalInfo(models.Model):
    GENRE = [
        (0, _('Akcja')),
        (1, _('Komedia')),
        (2, _('Dramat')),
        (3, _('Horror')),
        (4, _('Sci-fi')),
        (5, _('Inny')),
    ]

    duration = models.PositiveIntegerField(default=0)
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRE)


class Rating(models.Model):
    comment = models.TextField(default='', blank=True)
    stars = models.SmallIntegerField(default=5)
    movie = models.ForeignKey(Movie, related_name='rating', on_delete=models.CASCADE)


class Actor(models.Model):
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    movies = models.ManyToManyField(Movie, related_name='actors')
