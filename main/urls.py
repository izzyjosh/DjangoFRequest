from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
        path("",views.home,name="home"),
        path("add_friend/<uuid:user_id>/",views.frequest,name="request"),
        path("accept/<uuid:request_id>/",views.acceptrequest,name="accept"),
        path("delete/<uuid:request_id>/",views.rejectrequest,name="reject"),
        path("request/",views.allrequest,name="allrequest")
        ]
