from django.contrib.auth.models import User
from django.conf import settings

import decimal

from valuenetwork.valueaccounting.models import \
    AgentType, EconomicAgent, AgentUser, EventType, EconomicResourceType, \
    Unit, AgentResourceRoleType

from work.models import Project

# It creates the needed initial data to run the work tests:
# admin_user, admin_agent, Freedom Coop agent, FC Membership request agent, ...
def initial_test_data():
    # To see debugging errors in the browser while making changes in the test.
    setattr(settings, 'DEBUG', True)

    # We want to reuse the test db, to be faster (manage.py test --keepdb),
    # so we create the objects only if they are not in test db.
    try:
        admin_user = User.objects.get(username='admin_user')
    except User.DoesNotExist:
        admin_user = User.objects.create_superuser(
            username='admin_user',
            password='admin_passwd',
            email='admin_user@example.com'
        )
        print "t- created User: 'admin _user'"

    # AgentTypes
    individual_at, c = AgentType.objects.get_or_create(
        name='Individual', party_type='individual', is_context=False)
    if c: print "t- created AgentType: 'Individual'"

    project_at, c = AgentType.objects.get_or_create(
        name='Project', party_type='team', is_context=True)
    if c: print "t- created AgentType: 'Project'"

    cooperative_at, c = AgentType.objects.get_or_create(
        name='Cooperative', party_type='organization', is_context=True)
    if c: print "t- created AgentType: 'Cooperative'"

    # EconomicAgent for admin_user related to him/her.
    admin_ea, c = EconomicAgent.objects.get_or_create(name='admin_agent',
        nick='admin_agent', agent_type=individual_at,  is_context=False)
    if c: print "t- created EconomicAgent: 'admin_agent'"

    au, c = AgentUser.objects.get_or_create(agent=admin_ea, user=admin_user)
    if c: print "t- created AgentUser: "+str(au)

    # EconomicAgent for Freedom Coop
    fdc, c = EconomicAgent.objects.get_or_create(name='Freedom Coop',
        nick='Freedom Coop', agent_type=cooperative_at, is_context=True)
    if c: print "t- created EconomicAgent: 'Freedom Coop'"

    # Project for FreedomCoop
    pro, c = Project.objects.get_or_create(agent=fdc, joining_style="moderated", fobi_slug='freedom-coop')
    if c: print "t- created Project: "+str(pro)

    # EconomicAgent for Memebership Request
    fdcm, c = EconomicAgent.objects.get_or_create(name='FreedomCoop Membership',
        nick=settings.SEND_MEMBERSHIP_PAYMENT_TO, agent_type=project_at, is_context=True)
    if c: print "t- created EconomicAgent: 'FreedomCoop Membership'"

    # EventType for todos
    et, c = EventType.objects.get_or_create(name='Todo', label='todo',
        relationship='todo', related_to='agent', resource_effect='=')
    if c: print "t- created EventType: 'Todo'"

    ert, c = EconomicResourceType.objects.get_or_create(name='something_with_Admin', behavior='work')
    if c: print "t- created EconomicResourceType: "+str(ert)

    # Manage FairCoin
    FC_unit = Unit.objects.get(name='FairCoin') #_or_create(unit_type='value', name='FairCoin', abbrev='fair')
    #if c: print "t- created Unit: 'FairCoin'"

    ert = EconomicResourceType.objects.get(name='FairCoin') #, unit=FC_unit, unit_of_use=FC_unit,
        #value_per_unit_of_use=decimal.Decimal('1.00'), substitutable=True, behavior='dig_acct')
    #if c: print "t- created EconomicResourceType: 'FairCoin'"

    arrt, c = AgentResourceRoleType.objects.get_or_create(name='Owner', is_owner=True)
    if c: print "t- created AgentResourceRoleType: "+str(arrt)

