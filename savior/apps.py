from django.apps import AppConfig
import os
from django.conf import settings

# class SaviorConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'savior'

class TranslatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'savior'
    path = os.path.join(settings.BASE_DIR, 'translator')
