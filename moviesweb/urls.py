from django.urls import path
from moviesweb.views import add_movie, edit_movie, delete_movie, custom_form, AllMoviesView

urlpatterns = [
    path('all/', AllMoviesView.as_view(), name='all_movies'),
    path('add/', add_movie, name='add_movie'),
    path('edit/<int:id>', edit_movie, name='edit_movie'),
    path('delete/<int:id>', delete_movie, name='delete_movie'),
    path('custom/', custom_form, name='custom'),
]
