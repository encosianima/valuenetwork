from django.apps import AppConfig
from django.db.models.signals import post_migrate
#from django_comments.models import Comment
from django_comments.signals import comment_was_posted #, comment_will_be_posted
import logging
logger = logging.getLogger("ocp")

class WorkAppConfig(AppConfig):
    name = 'work'
    verbose_name = 'Work'

    def ready(self):
        super(WorkAppConfig, self).ready()

        from work.models import create_unit_types, create_exchange_skills
        from general.models import create_general_types
        from work.signals import comment_notification

        post_migrate.connect(create_general_types, sender=self)
        post_migrate.connect(create_unit_types, sender=self)
        post_migrate.connect(create_exchange_skills, sender=self)
        comment_was_posted.connect(comment_notification, sender=self) #Comment)
        #comment_will_be_posted.connect(pre_comment, sender=Comment)
        logger.debug("Connected signals to post_migrate and comment_was_posted")
