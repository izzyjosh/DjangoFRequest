from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm


class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    email = forms.EmailField(
            label="",
            required=True,
            widget = forms.EmailInput(attrs={
                "placeholder":"Valid Email",
                "type":"email",
                "name":"email",
                "class":"form-control m-2",
                })
            )
    class Meta:
        model = MyUser
        fields = ("email")

class CustomSetPasswordForm(SetPasswordForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    newpassword1 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"password",
            "type":"password",
            "name":"password1",
            "class":"form-control m-2",
            })
        )

    newpassword2 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"confirm password",
            "type":"password",
            "name":"password1",
            "class":"form-control m-2",
            })
        )

    class Meta:
        model = MyUser
        fields = ("newpassword1","newpassword2")


class UserRegistrationForm(UserCreationForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


    username = forms.CharField(
            label="",
            required=True,
            help_text="",
            widget = forms.TextInput(attrs={
                "placeholder":"username",
                "name":"username",
                "class":"username",
                "type":"text",
                })
            )

    email = forms.EmailField(
        label="",
        required=True,
        widget = forms.TextInput(attrs={
            "placeholder":"Email",
            "type":"email",
            "name":"email",
            "class":"email",
            })
        )

    password1 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"password",
            "type":"password",
            "name":"password1",
            "class":"password",
            })
        )
    
    password2 = forms.CharField(
        label="",
        required=True,
        help_text="",
        widget = forms.PasswordInput(attrs={
            "placeholder":"confirm password",
            "type":"password",
            "name":"password1",
            "class":"password",
            })
        )

    class Meta:
        model = MyUser
        fields = ("email","username")




