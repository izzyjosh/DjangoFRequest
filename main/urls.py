from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from django.conf import settings 
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
        path("",views.home,name="home"),
        path("add_friend/<uuid:user_id>/",views.frequest,name="request"),
        path("added/<uuid:user_id>/",views.added,name="added"),
        path("accept/<uuid:request_id>/",views.acceptrequest,name="accept"),
        path("delete/<uuid:request_id>/",views.rejectrequest,name="reject"),
        path("request/",views.allrequest,name="allrequest"),
        path("friendslist/",views.friendslist,name="friendslist"),
        ] + static(settings.MEDIA_URL,
                   document_root=settings.MEDIA_ROOT)
