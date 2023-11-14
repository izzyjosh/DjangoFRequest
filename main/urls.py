from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = "main"

urlpatterns = [
        path("",cache_page(60 * 5)(views.home),name="home"),
        path("add_friend/<uuid:user_id>/",views.frequest,name="request"),
        path("added/<uuid:user_id>/",views.added,name="added"),
        path("accept/<uuid:request_id>/",views.acceptrequest,name="accept"),
        path("delete/<uuid:request_id>/",views.rejectrequest,name="reject"),
        path("request/",views.allrequest,name="allrequest")
        ]
