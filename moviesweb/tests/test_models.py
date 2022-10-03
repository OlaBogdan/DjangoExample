from django.test import TestCase

from moviesweb.models import Movie


class ModelsTests(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(title='testowy', description='test', year=2022)

    def test_movie_str(self):
        self.assertEqual(str(self.movie), 'testowy (2022)')
