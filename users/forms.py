from django import forms


class NameForm(forms.Form):
    user_name = forms.CharField(label='The username contains:', max_length=100)
