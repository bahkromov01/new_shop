from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_delete, sender=User)
def delete_token(sender, instance, **kwargs):
    instance.delete()
    Token.objects.filter(user=instance).delete()
