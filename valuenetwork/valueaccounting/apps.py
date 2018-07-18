from django.apps import AppConfig
from django.db.models.signals import post_migrate

from valuenetwork.valueaccounting import signals

class ValueAccountingAppConfig(AppConfig):
    name = 'valuenetwork.valueaccounting'
    verbose_name = "Value Accounting"

    def ready(self):
        super(ValueAccountingAppConfig, self).ready()

        from valuenetwork.valueaccounting.models import create_agent_types, create_agent_association_types, create_use_cases, create_event_types, create_usecase_eventtypes
        from valuenetwork.valueaccounting.signals import create_notice_types

        post_migrate.connect(create_notice_types, sender=self)
        post_migrate.connect(create_agent_types, sender=self)
        post_migrate.connect(create_agent_association_types, sender=self)
        post_migrate.connect(create_use_cases, sender=self)
        post_migrate.connect(create_event_types, sender=self)
        post_migrate.connect(create_usecase_eventtypes, sender=self)

