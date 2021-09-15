from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    email = models.CharField(blank=False, unique=True, max_length=128,
                             help_text='Обязательное поле. Не более 128 символов.')
