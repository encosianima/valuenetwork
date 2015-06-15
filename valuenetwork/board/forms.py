import sys
import datetime
from decimal import *
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from valuenetwork.valueaccounting.models import *


PAID_CHOICES = (('paid', 'Paid for'),
    ('later', 'Will pay later'),
    ('never', 'Payment not needed'))

class ExchangeFlowForm(forms.Form):
    event_date = forms.DateField(required=True, 
        label=_("Transfer Date"),
        widget=forms.TextInput(attrs={'class': 'item-date date-entry',}))
    to_agent = forms.ModelChoiceField(required=False,
        queryset=EconomicAgent.objects.all(),
        label="Transfer To", 
        widget=forms.Select(
            attrs={'class': 'chzn-select'}))
    quantity = forms.DecimalField(required=True,
        label="Quantity",
        widget=forms.TextInput(attrs={'value': '1', 'class': 'quantity  input-small'}))
    value = forms.DecimalField(
        help_text="Total value of the transfer, not value for each unit.",
        widget=forms.TextInput(attrs={'class': 'value input-small',}))
    unit_of_value = forms.ModelChoiceField(
        empty_label=None,
        queryset=Unit.objects.filter(unit_type='value'))
    notes = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class': 'item-description',}))
    paid = forms.MultipleChoiceField(required=True,
        widget=forms.RadioSelect, choices=PAID_CHOICES)
        
    def __init__(self, assoc_type_identifier=None, context_agent=None, qty_help=None, *args, **kwargs):
        super(ExchangeFlowForm, self).__init__(*args, **kwargs)
        #import pdb; pdb.set_trace()
        if context_agent and assoc_type_identifier:
            self.fields["to_agent"].queryset = context_agent.all_has_associates_by_type(assoc_type_identifier=assoc_type_identifier)   
        if qty_help:
            self.fields["quantity"].help_text = qty_help

class ZeroOutForm(forms.Form):
    zero_out = forms.BooleanField(
        required=False,
        label="Last harvest of this resource type on this farm (zero out farm inventory)", 
        widget=forms.CheckboxInput())
    
class PlanProcessForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-xlarge',}))
    start_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'input-small date-entry',}))
    end_date = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'input-small date-entry',}))
    
    class Meta:
        model = Process
        fields = ('name', 'start_date', 'end_date')
        
class AvailableForm(forms.ModelForm):
    event_date = forms.DateField(
        required=True, 
        label="Available on",
        widget=forms.TextInput(attrs={'class': 'input-small date-entry', }))
    from_agent = forms.ModelChoiceField(
        required=True,
        label="Farm", 
        queryset=EconomicAgent.objects.all(),
        widget=forms.Select(
            attrs={'class': 'chzn-select'}))
    resource_type = forms.ModelChoiceField(
        queryset=EconomicResourceType.objects.all(),
        widget=forms.Select(
            attrs={'class': 'resource-type-selector resourceType chzn-select input-large'}))
    quantity = forms.DecimalField(required=True,
        label="Approximate quantity in pounds",
        widget=forms.TextInput(attrs={'value': '1', 'class': 'quantity  input-small'}))
    description = forms.CharField(
        required=False,
        label="Notes", 
        widget=forms.Textarea(attrs={'class': 'item-description',}))
        
    class Meta:
        model = EconomicEvent
        fields = ('from_agent', 'resource_type', 'event_date', 'quantity', 'description')

    def __init__(self, pattern=None, context_agent=None, *args, **kwargs):
        super(AvailableForm, self).__init__(*args, **kwargs)
        #import pdb; pdb.set_trace()
        if pattern:
            self.pattern = pattern
            et = EventType.objects.get(name="Make Available")
            self.fields["resource_type"].queryset = pattern.get_resource_types(event_type=et)
        if context_agent:
            self.fields["from_agent"].queryset = context_agent.all_has_associates_by_type(assoc_type_identifier="Grower")
 
