from django.contrib.auth.models import User
from rest_framework import serializers

from moviesweb.models import Movie


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class MovieSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description']
