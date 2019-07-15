"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=254,
                                label=_("Логин"),
                                widget=forms.TextInput({
                                   'class': 'form-control'}))
    password = forms.CharField(label=_("Пароль"),
                                widget=forms.PasswordInput({
                                   'class': 'form-control'}))
    first_name = forms.CharField(max_length=254,
                                label=_("Имя"),
                                widget=forms.TextInput({
                                   'class': 'form-control'}))
    last_name = forms.CharField(max_length=254,
                                label=_("Фамилия"),
                                widget=forms.TextInput({
                                   'class': 'form-control'}))
    email = forms.CharField(max_length=254,
                                label=_("Email"),
                                widget=forms.TextInput({
                                   'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
