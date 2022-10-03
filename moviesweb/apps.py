from django.apps import AppConfig


class MovieswebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moviesweb'

    def ready(self):
        import moviesweb.signals
