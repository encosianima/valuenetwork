from django.apps import AppConfig
from django.db.models.signals import post_migrate

class WorkAppConfig(AppConfig):
    name = 'work'
    verbose_name = 'Work'

    def ready(self):
        super(WorkAppConfig, self).ready()

        from work.models import create_unit_types, create_exchange_skills
        from general.models import create_general_types

        post_migrate.connect(create_general_types, sender=self)
        post_migrate.connect(create_unit_types, sender=self)
        post_migrate.connect(create_exchange_skills, sender=self)
