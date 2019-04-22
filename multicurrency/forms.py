from django import forms
from django.utils.translation import ugettext_lazy as _


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
