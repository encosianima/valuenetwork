from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from work.models import JoinRequest
from multicurrency.models import MulticurrencyAuth

class MulticurrencyAuthForm(forms.Form):
    loginname = forms.CharField(
        max_length=32,
        label = _("Wallet Username"),
        widget=forms.TextInput(
            attrs={'class': 'required-field input-xxlarge', }))
    wallet_password = forms.CharField(
        max_length=32,
        label = _("Wallet Password"),
        widget=forms.PasswordInput(
            attrs={'class': 'required-field input-xxlarge', }))


class MulticurrencyAuthDeleteForm(forms.Form):
    hidden_delete = forms.CharField(
        widget=forms.HiddenInput(), initial='delete')


class MulticurrencyAuthCreateForm(forms.Form):
    hidden_create = forms.CharField(widget=forms.HiddenInput(),
                                    initial='create')
    username = forms.CharField(max_length=32, widget=forms.TextInput(
        attrs={'class': 'required-field input-xxlarge', }))
    email = forms.EmailField()
    password = forms.CharField(min_length=6, max_length=32,
                               widget=forms.PasswordInput)

class PaySharesForm(forms.Form):
    amount = forms.CharField(widget=forms.HiddenInput(),
                                    initial=0)
    unit = forms.CharField(widget=forms.HiddenInput(),
                                    initial='')
    jnreq_id = forms.CharField(widget=forms.HiddenInput(),
                                    initial=0)
    auth_id = forms.CharField(widget=forms.HiddenInput(),
                                    initial=0)
    def __init__(self, reqdata=None, *args, **kwargs):
        super(PaySharesForm, self).__init__(*args, **kwargs)
        if reqdata and 'jnreq_id' in reqdata:
            jnreq = JoinRequest.objects.get(id=reqdata['jnreq_id'])
            if reqdata['auth_id']:
                if jnreq.agent:
                    auth = MulticurrencyAuth.objects.get(id=reqdata['auth_id'])
                    if auth.auth_user == jnreq.multiwallet_user():
                        if auth in jnreq.agent.multicurrencyauth_set.all():
                            #import pdb; pdb.set_trace()
                            self.fields['amount'].initial = reqdata['amount'] #jnreq.payment_pending_to_pay()
                            self.fields['unit'].initial = reqdata['unit'] #jnreq
                            self.fields['jnreq_id'].initial = jnreq.id
                            self.fields['auth_id'].initial = auth.id
                        else:
                            raise ValidationError("the auth is not related the jnreq.agent !")
                    else:
                        raise ValidationError("the auth.user is not the jnreq.multiwallet_user !")
                else:
                    raise ValidationError("the jnreq has no agent !")
            else:
                raise ValidationError("missing auth !")
        else:
            pass #raise ValidationError("missing jnreq !")



