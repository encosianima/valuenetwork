from modeltranslation.translator import translator, TranslationOptions
from .models import EconomicAgent

class EconomicAgentTranslationOptions(TranslationOptions):
    fields = ('name', 'nick', 'url', 'description', 'address', 'email', 'phone_primary', 'photo_url')

translator.register(EconomicAgent, EconomicAgentTranslationOptions)
