from django import forms


class WikiForm(forms.Form):
    query = forms.CharField()

