from typing import Type

from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from mkdata.models import Work, AddedWork

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
        fields = ('like', 'joy','anger','sadness','fun','tech_constitution','tech_story','tech_character','tech_speech','tech_picture')

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['like'].widget.attrs['class'] = 'input'
        self.fields['joy'].widget.attrs['class'] = 'input'
        self.fields['anger'].widget.attrs['class'] = 'input'
        self.fields['sadness'].widget.attrs['class'] = 'input'
        self.fields['fun'].widget.attrs['class'] = 'input'
        self.fields['tech_constitution'].widget.attrs['class'] = 'input'
        self.fields['tech_story'].widget.attrs['class'] = 'input'
        self.fields['tech_character'].widget.attrs['class'] = 'input'
        self.fields['tech_speech'].widget.attrs['class'] = 'input'
        self.fields['tech_picture'].widget.attrs['class'] = 'input'

        ###
        #self.pk = kwargs.pop('pk')
        #super(CollectDataForm, self).__init__(*args, **kwargs)
        #####

    def update_database(self):
        for items in self.fields:
            self.model.like += self.fields['like'].widget.attrs['class']
    '''



class AddWorkForm(forms.ModelForm):
    class Meta:
        model = AddedWork
        fields = ('like', 'joy', 'anger', 'sadness', 'fun', 'tech_constitution', 'tech_story', 'tech_character', 'tech_speech', 'tech_picture' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'

'''
class SelectGenreForm(forms.ModelForm):
    class Meta:
        model = AddedWork
        fields = ('genre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'
'''
