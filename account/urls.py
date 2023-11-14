from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
        path("signup/",views.signup,name="signup"),
        path("signin/",auth_views.LoginView.as_view(template_name="signin.html"),name="login"),
        path("logout/",auth_views.LogoutView.as_view(),name="logout"),
        ]
