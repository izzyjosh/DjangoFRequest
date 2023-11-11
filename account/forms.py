from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm


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
