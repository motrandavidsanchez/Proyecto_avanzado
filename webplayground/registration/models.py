from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'
