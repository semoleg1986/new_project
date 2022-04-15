from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя', "class":"myfield", 'style':'text-transform: lowercase;'}))
    password = forms.CharField(label="Пароль",widget = forms.PasswordInput(attrs={'placeholder': 'Пароль', "class":"myfield"}))

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Старый пароль', 'class': "myfield"}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль', 'class': "myfield"}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Еще раз введите пароль', 'class': "myfield"}))

class PasswordResetingForm(PasswordResetForm):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Ваша электронная почта', 'class': "myfield", 'type': 'email', 'name': 'email'}))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль', 'class': "myfield"}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Еще раз введите пароль', 'class': "myfield"}))

from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Имя логина", widget=forms.TextInput(attrs={'placeholder': 'Имя логина', "class":"myfield", 'style':'text-transform: lowercase;'}))
    def clean_username(self):
        data = self.cleaned_data['username']
        return data.lower()
    first_name = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя', "class":"myfield"}))

    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Ваша электронная почта', 'class': "myfield", 'type': 'email', 'name': 'email'}))
    password = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль', 'class': "myfield"}))
    password2 = forms.CharField(label='Repeat password',  widget=forms.PasswordInput(attrs={'placeholder': 'Введите еще раз пароль', 'class': "myfield"}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


from .models import Profile

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'placeholder': 'Имя', "class":"myfield"}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'placeholder': 'Фамилия', "class":"myfield"}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Ваша электронная почта', 'class': "myfield", 'type': 'email', 'name': 'email'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# YEARS= [x for x in range(1940,2021)]
import datetime
year = datetime.date.today().year

class ProfileEditForm(forms.ModelForm):
    # date_of_birth = forms.DateField(widget=forms.DateInput(format=('%d.%m.%Y'),attrs={'placeholder': 'Дата рождение: 01/01/1900 ', "class":"myfield", 'onfocus':"(this.type='date')", 'onblur':"(this.type='text')", 'value':"YYYY-MM-DD"}))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(year, year-101, -1),attrs={'placeholder': 'Дата рождение: 01/01/1900', 'class':'myfield', 'style':'width:93px; background-color:white;'}))
    photo = forms.ImageField()
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
