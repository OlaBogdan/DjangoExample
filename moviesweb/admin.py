from django import forms
from django.contrib import admin
from django.contrib.admin.helpers import ActionForm

from moviesweb.models import Movie, AdditionalInfo, Rating, Actor


class ChangeYearForm(ActionForm):
    new_year = forms.IntegerField()


@admin.action(description='Change selected movies year')
def change_movie_year(modeladmin, request, queryset):
    new_year = request.POST.get('new_year', False)
    if new_year:
        queryset.update(year=new_year)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ["title", "description", "year"]
    # exclude = ["description"]
    list_display = ["title", "year", "imdb_rating"]
    list_filter = ('year', 'imdb_rating')
    search_fields = ["title", "description"]
    actions = [change_movie_year]
    action_form = ChangeYearForm


admin.site.register(AdditionalInfo)

admin.site.register(Rating)

admin.site.register(Actor)
