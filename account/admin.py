from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm

class CustomAdmin(UserAdmin):
    model = MyUser
    list_display = ["username","email","contact"]
    filter_vertical = ("friends",)

admin.site.register(MyUser,CustomAdmin)
