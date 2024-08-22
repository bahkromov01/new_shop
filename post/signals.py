from django.db.models.signals import post_save, post_delete,pre_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Post


@receiver(post_save, sender=Post)
@receiver(pre_save, sender=Post)
def clear_cache_on_save(sender, instance, **kwargs):
    cache.delete('post_list')
    post_id = instance.id
    cache.delete(f'post_detail_{post_id}')


@receiver(post_delete, sender=Post)
@receiver(pre_save, sender=Post)
def clear_cache_on_delete(sender, instance, **kwargs):
    cache_key = f'post_{instance.title}'
    post_id = instance.id
    cache.clear(cache_key, post_id)