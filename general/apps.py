from django.apps import AppConfig

class GeneralAppConfig(AppConfig):
    name = 'general'
    verbose_name = 'General'

    def ready(self):
        super(GeneralAppConfig, self).ready()
        #import work.signals
