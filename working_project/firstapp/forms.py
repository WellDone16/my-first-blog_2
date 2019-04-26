from django import forms

class UserForm(forms.Form):
    userfile = forms.MultipleChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))
