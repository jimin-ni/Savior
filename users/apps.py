from django.apps import AppConfig
import os
from django.conf import settings

# class UsersConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'users'

class TranslatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'translator'
    path = os.path.join(settings.BASE_DIR, 'translator')
