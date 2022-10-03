from django.test import TestCase
from django.urls import reverse, resolve

from moviesweb.views import all_movies, add_movie, edit_movie, delete_movie, custom_form


class UrlsTests(TestCase):

    def test_all_movies_url(self):
        url = reverse("all_movies")

        self.assertEqual(resolve(url).func, all_movies)

    def test_add_movie_url(self):
        url = reverse("add_movie")

        self.assertEqual(resolve(url).func, add_movie)

    def test_edit_movie_url(self):
        url = reverse("edit_movie", kwargs={'id': 1})

        self.assertEqual(resolve(url).func, edit_movie)

    def test_delete_movie_url(self):
        url = reverse("delete_movie", kwargs={'id': 1})

        self.assertEqual(resolve(url).func, delete_movie)

    def test_custom_url(self):
        url = reverse("custom")

        self.assertEqual(resolve(url).func, custom_form)
