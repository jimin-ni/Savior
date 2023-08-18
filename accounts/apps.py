from django.apps import AppConfig
import os
from django.conf import settings

# class AccountsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'accounts'

class TranslatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    path = os.path.join(settings.BASE_DIR, 'translator')
