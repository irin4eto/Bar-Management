from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
from users.models import UserProfile
from django import forms


class UserForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(
                             max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))
    ROLE = (
        ('M', 'Управител'),
        ('W', 'Сервитьор'),
        ('B', 'Барман')
    )
    role = forms.ChoiceField(required=True, choices=ROLE)
    first_name = forms.CharField(required=True, max_length=30,
                                 error_messages={'required':
                                                 "Please enter your " +
                                                 "first name"})
    last_name = forms.CharField(required=True, max_length=30,
                                error_messages={'required': 'Please enter' +
                                                'your last name'})

    class Meta:
        model = User

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=
                                    self.cleaned_data
                                    ['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please" +
                                      "try another one."))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, *args, **kw):
        super(UserForm, self).save(*args, **kw)
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.role = self.cleaned_data.get('role')
        self.instance.user.save()

    """def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            self.instance.user.save()
        return user"""


"""class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User

    def clean_password(self):
        return self.initial["password"]"""


class UserProfileForm(forms.Form):
    ROLE = (
        ('M', 'Управител'),
        ('W', 'Сервитьор'),
        ('B', 'Барман')
    )
    role = forms.ChoiceField(required=True, choices=ROLE)
    """first_name = forms.CharField(required=True, max_length=30,
                                 error_messages={'required':
                                                 "Please enter your " +
                                                 "first name"})
    last_name = forms.CharField(required=True, max_length=30,
                                error_messages={'required': 'Please enter' +
                                                'your last name'})"""

    class Meta:
        model = UserProfile


class LoginForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=
                                dict(required=True, max_length=30)),
                                label=_("Username"),
                                error_messages={'invalid':
                                                _(str("This value must" +
                                                      "contain only letters," +
                                                      "numbers and" +
                                                      "underscores."))})
    password = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password"))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(
                             max_length=30)), label=_("Email address"))
