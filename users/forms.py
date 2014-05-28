from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from models import UserProfile
from django import forms


class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User

    def clean_password(self):
        return self.initial["password"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (' email', 'role', 'first_name', 'last_name')
