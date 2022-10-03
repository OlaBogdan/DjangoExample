import logging

from django.views.generic import TemplateView, ListView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.translation import gettext as _
from rest_framework import viewsets

from moviesweb.models import Movie
from moviesweb.forms import MovieForm, AdditionalInfoForm, RatingForm, CustomForm
from moviesweb.serializers import UserSerializers, MovieSerializers
from moviesweb.signals import custom_signal

logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)
log_file_handler = logging.FileHandler('logs/views.log')
log_file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class AllMoviesView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'moviesweb/movies.html'

    def dispatch(self, request, *args, **kwargs):
        custom_signal.send(sender=Movie, test='test')

        return super(AllMoviesView, self).dispatch(request, *args, **kwargs)


@login_required
def add_movie(request):
    form_movie = MovieForm(request.POST or None, request.FILES or None)
    form_additional_info = AdditionalInfoForm(request.POST or None)

    if all([form_movie.is_valid(), form_additional_info.is_valid()]):
        movie = form_movie.save(commit=False)
        additional_info = form_additional_info.save()
        movie.additional_info = additional_info
        movie.save()

        logger.info(_('Dodano film.'))

        messages.success(request, _("Dodano film"))

        return redirect(all_movies)

    context = {
        'form_movie': form_movie,
        'form_additional_info': form_additional_info,
        'title': _('Dodaj film'),
    }

    return render(request, 'moviesweb/form.html', context)


@login_required
def edit_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    form_movie = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    form_additional_info = AdditionalInfoForm(request.POST or None, instance=movie.additional_info)
    form_rating = RatingForm(request.POST or None)

    if request.method == 'POST' and 'stars' in request.POST:
        rating = form_rating.save(commit=False)
        rating.movie = movie
        rating.save()

    if all([form_movie.is_valid(), form_additional_info.is_valid()]):
        movie = form_movie.save(commit=False)
        additional_info = form_additional_info.save()
        movie.additional_info = additional_info
        movie.save()

        return redirect(all_movies)

    rating = movie.rating.all()
    actors = movie.actors.all()

    context = {
        'form_movie': form_movie,
        'form_additional_info': form_additional_info,
        'title': _('Edytuj film'),
        'rating': rating,
        'form_rating': form_rating,
        'actors': actors
    }

    return render(request, 'moviesweb/form.html', context)


@login_required
def delete_movie(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == 'POST':
        movie.delete()
        return redirect(all_movies)

    context = {
        'movie': movie
    }

    return render(request, 'moviesweb/confirm.html', context)


@login_required
def custom_form(request):
    form = CustomForm(request.POST or None)

    if form.is_valid():
        print('valid')

    context = {
        'form': form,
    }

    return render(request, 'moviesweb/custom_form.html', context)
