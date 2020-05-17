from typing import Type

from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from mkdata.models import Work

UserModel = get_user_model()

'''
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['username'].widget.attrs['class'] = 'input'
       self.fields['password'].widget.attrs['class'] = 'input'
'''


class CollectDataForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('like', 'joy','anger','sadness','fun','constitution','story','character','speech','picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['like'].widget.attrs['class'] = 'input'
        self.fields['joy'].widget.attrs['class'] = 'input'
        self.fields['anger'].widget.attrs['class'] = 'input'
        self.fields['sadness'].widget.attrs['class'] = 'input'
        self.fields['fun'].widget.attrs['class'] = 'input'
        self.fields['constitution'].widget.attrs['class'] = 'input'
        self.fields['story'].widget.attrs['class'] = 'input'
        self.fields['charecter'].widget.attrs['class'] = 'input'
        self.fields['speech'].widget.attrs['class'] = 'input'
        self.fields['picture'].widget.attrs['class'] = 'input'

