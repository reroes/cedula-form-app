from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class CedulaInfo(models.Model):
    """
    This model contains two extra fields that will
    be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    @reroes

    """
    user = models.OneToOneField(USER_MODEL, null=True)

    identificacion_user = models.CharField(
        verbose_name="Identification",
        max_length=200,
    )
    telefono = models.CharField(
        verbose_name="Telephone",
        max_length=200,
    )
