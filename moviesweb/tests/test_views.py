from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ViewsTests(TestCase):

    def test_all_movies_view(self):
        url = reverse("all_movies")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies.html")

    def test_add_movie_url_not_logged_in(self):
        response = self.client.get(reverse("add_movie"))

        self.assertEqual(response.status_code, 302)

    def test_add_movie_url_logged_in(self):
        User.objects.create_superuser(username='admin', password='1234')
        url = reverse("add_movie")
        self.client.login(username='admin', password='1234')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form.html")
