from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver, Signal

from moviesweb.models import Movie

custom_signal = Signal()


@receiver(post_save, sender=Movie)
def movie_post_save(sender, instance, **kwargs):
    print('just save movie')


@receiver(request_finished)
def page_loaded(sender, **kwargs):
    print('page is loaded')


@receiver(custom_signal)
def custom_signal_receiver(sender, **kwargs):
    print(kwargs)
