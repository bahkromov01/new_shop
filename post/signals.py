from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Post


@receiver(post_save, sender=Post)
def clear_cache_on_save(sender, instance, **kwargs):
    cache_key = f'post_{instance.title}'
    cache.delete(cache_key)


@receiver(post_delete, sender=Post)
def clear_cache_on_delete(sender, instance, **kwargs):
    cache_key = f'post_{instance.title}'
    cache.delete(cache_key)