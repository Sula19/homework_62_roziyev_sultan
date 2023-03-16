from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, required=True, label='Логин')
    password = forms.CharField(max_length=70, required=True, label='Пароль', widget=forms.PasswordInput)
