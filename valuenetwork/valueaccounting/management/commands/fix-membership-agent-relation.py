# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.db.models import Count

from valuenetwork.valueaccounting.models import EconomicAgent
from work.models import MembershipRequest

class Command(BaseCommand):
    help = "Fix memberships which do not have a relation to their agent"

    def handle(self, *args, **options):

        dupes = MembershipRequest.objects.values('requested_username').annotate(Count('id')).order_by().filter(id__count__gt=1)
        membership = MembershipRequest.objects.filter(agent_id=None).exclude(requested_username__in=[item['requested_username'] for item in dupes])
        for m in membership:
            agent = EconomicAgent.objects.filter(nick=m.requested_username)
            if agent.count() == 1:
                print "* Fixing membership to agent relation for: ", m.email_address
                m.agent = agent[0]
                m.save()
