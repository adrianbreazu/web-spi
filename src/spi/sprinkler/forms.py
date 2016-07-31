from django import forms

class SubmitForm(forms.Form):
    ceva_text = forms.CharField()