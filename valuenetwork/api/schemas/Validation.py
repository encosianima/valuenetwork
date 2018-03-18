#
# Graphene schema for exposing Validation model
#
# @package: OCP
# @since:   2017-06-22
#

import graphene
import datetime
from valuenetwork.valueaccounting.models import EconomicAgent, EconomicEvent, AgentUser
from validation.models import Validation as ValidationProxy
from valuenetwork.api.types.Validation import Validation
#from valuenetwork.api.models import formatAgent
from six import with_metaclass
from django.contrib.auth.models import User
from .Auth import AuthedInputMeta, AuthedMutation
from django.core.exceptions import PermissionDenied


class Query(graphene.AbstractType):

    validation = graphene.Field(Validation,
                                id=graphene.Int())

    all_validations = graphene.List(Validation)

    def resolve_validation(self, args, *rargs):
        id = args.get('id')
        if id is not None:
            validation = ValidationProxy.objects.get(pk=id)
            if validation:
                return validation
        return None

    def resolve_all_validations(self, args, context, info):
        return ValidationProxy.objects.all()


class CreateValidation(AuthedMutation):
    class Input(with_metaclass(AuthedInputMeta)):
        economic_event_id = graphene.Int(required=True)
        validated_by_id = graphene.Int(required=True)

    validation = graphene.Field(lambda: Validation)

    @classmethod
    def mutate(cls, root, args, context, info):
        economic_event_id = args.get('economic_event_id')
        validated_by_id = args.get('validated_by_id')

        economic_event = EconomicEvent.objects.get(pk=economic_event_id)
        agent = EconomicAgent.objects.get(pk=validated_by_id)
        validation = ValidationProxy(
            event=economic_event,
            validated_by=agent,
        )

        user_agent = AgentUser.objects.get(user=context.user).agent
        is_authorized = user_agent.is_authorized(object_to_mutate=validation)
        if is_authorized:
            validation.save()  
        else:
            raise PermissionDenied('User not authorized to perform this action.')

        return CreateValidation(validation=validation)


class DeleteValidation(AuthedMutation):
    class Input(with_metaclass(AuthedInputMeta)):
        id = graphene.Int(required=True)

    validation = graphene.Field(lambda: Validation)

    @classmethod
    def mutate(cls, root, args, context, info):
        id = args.get('id')
        validation = ValidationProxy.objects.get(pk=id)
        if validation:
            user_agent = AgentUser.objects.get(user=context.user).agent
            is_authorized = user_agent.is_authorized(object_to_mutate=validation)
            if is_authorized:
                validation.delete() 
            else:
                raise PermissionDenied('User not authorized to perform this action.')

        return DeleteValidation(validation=validation)
