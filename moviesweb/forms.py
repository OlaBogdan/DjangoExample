from django import forms
from django.forms import ModelForm, Form
from django.utils.translation import gettext as _

from moviesweb.models import Movie, AdditionalInfo, Rating
from moviesweb.validators import validate_year


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'premiere', 'year', 'imdb_rating']


class AdditionalInfoForm(ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['duration', 'genre']


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['stars', 'comment']


class CustomForm(Form):
    title = forms.CharField(label=_('Tytuł'), max_length=64)
    year = forms.IntegerField(label=_('Rok produkcji'))

    def clean_year(self):
        year = self.cleaned_data.get('year', -1)
        year = validate_year(year)

        return year
