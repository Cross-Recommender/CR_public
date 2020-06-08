from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
import random, string

UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['username'].widget.attrs['class'] = 'input'
       self.fields['password'].widget.attrs['class'] = 'input'

class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'

class GuestCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Q = randomname(random.randint(15,25))
        mail = randomname(random.randint(10,14))+'@cross.con'
        self.fields['password1'].initial = Q
        self.fields['password2'].initial = Q
        self.fields['password1'].widget.render_value = True
        self.fields['password2'].widget.render_value = True
        self.fields['email'].initial = mail
        self.fields['email'].widget.render_value = True
        self.fields['email'].widget = forms.HiddenInput()
        self.fields['password1'].widget = forms.HiddenInput()
        self.fields['password2'].widget = forms.HiddenInput()
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'

'''
class GuestToRealUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'
'''

class MyPasswordChangeForm(PasswordChangeForm):
    """パスワード変更フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['old_password'].initial = self.user.Password
        self.fields['old_password'].widget.render_value = True

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email','twitter')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'


def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))