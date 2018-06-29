from django.apps import AppConfig
from django.db.models.signals import post_migrate

class GeneralAppConfig(AppConfig):
    name = 'general'
    verbose_name = 'General'

    def ready(self):
        super(GeneralAppConfig, self).ready()

        #from general.models import create_general_types

        #post_migrate.connect(create_general_types, sender=self)
        #import work.signals
