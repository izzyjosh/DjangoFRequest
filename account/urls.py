from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
        #path("",views.signin,name="signin"),
        path("signup/",views.signup,name="signup"),
        path("logout/",views.logout,name="logout"),
        path("",auth_views.LoginView.as_view(template_name="signin.html")),
        ]
