from decimal import Decimal

from django import forms
from django.utils.translation import ugettext_lazy as _

from valuenetwork.valueaccounting.models import EconomicAgent

class SendFairCoinsForm(forms.Form):
    quantity = forms.DecimalField(
        widget=forms.TextInput(attrs={'class': 'faircoins input-small',}),
        min_value=Decimal('0.00000001'),
        decimal_places=8,
        #localize=True
    )
    minus_fee = forms.BooleanField(required=False, initial=False, label="Substract fee to quantity")
    to_address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-xlarge',}),
        required=None
    )
    to_user = forms.ModelChoiceField(
        queryset=EconomicAgent.objects.filter(
            agent_resource_roles__role__is_owner=True,
            agent_resource_roles__resource__resource_type__behavior="dig_acct",
            agent_resource_roles__resource__faircoin_address__address__isnull=False),
        widget=forms.Select(
            attrs={'class': 'chzn-select'}),
            label=_("If you send to an OCP agent, choose it here to get the address:"),
            required=None,
    )
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'input-xxlarge',}))

    def __init__(self, agent=None, *args, **kwargs):
        super(SendFairCoinsForm, self).__init__(*args, **kwargs)

        if agent and agent.related_all_agents_queryset:
            ag_ids = []
            for ag in agent.related_all_agents_queryset():
                ag_ids.append(ag.id)
            self.fields['to_user'].queryset = EconomicAgent.objects.filter(
                id__in=ag_ids,
                agent_resource_roles__role__is_owner=True,
                agent_resource_roles__resource__resource_type__behavior="dig_acct",
                agent_resource_roles__resource__faircoin_address__address__isnull=False)
        self.fields['minus_fee'].initial  = False

    def clean(self):
        data = super(SendFairCoinsForm, self).clean()
        if data["to_address"]:
            data["to_address"] = data["to_address"].strip()
        data["quantity"] = Decimal(data["quantity"])
        if data["to_user"] and not data["to_address"]:
           touser = data["to_user"]
           if touser and touser.faircoin_address():
               data["to_address"] = touser.faircoin_address()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.utils import timezone

class ConfirmPasswordForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('confirm_password', )

    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        if not check_password(confirm_password, self.instance.password):
            self.add_error('confirm_password', 'Password does not match.')

    def save(self, commit=True):
        user = super(ConfirmPasswordForm, self).save(commit)
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user
