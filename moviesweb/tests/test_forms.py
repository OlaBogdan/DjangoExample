from django.test import TestCase

from moviesweb.forms import MovieForm


class FormsTests(TestCase):

    def test_movie_form(self):
        form = MovieForm({
            'title': 'testowy',
            'description': 'testowy',
            'premiere': '2022-01-01',
            'year': 2022,
            'imdb_rating': 5
        })

        self.assertTrue(form.is_valid())
