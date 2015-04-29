from alyan.models import Bicycle, BicyclePhoto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import EmailField, CharField
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(UserCreationForm):
    email = EmailField(label=_("Email address"), required=True, help_text=_("Required."))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProfileForm(RegistrationForm):
    fullname = CharField(label=_("Email address"), required=True, help_text=_("Required."))

    class Meta:
        model = User
        fields = ("username", "email", "fullname", "password1", "password2")

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        user.fullname = self.cleaned_data["fullname"]
        if commit:
            user.save()
        return user


class BicycleForm(forms.ModelForm):
    new_image = forms.ImageField(required=False)

    class Meta:
        model = Bicycle
        fields = ["brand", "model", "year", "color", "note", "city", "serial_number", "new_image"]

    def save(self, commit=True):
        if self.cleaned_data['new_image']:
            BicyclePhoto(bicycle=super(BicycleForm, self), photo=self.cleaned_data['new_image'])


        return super(BicycleForm, self).save(commit=commit)

