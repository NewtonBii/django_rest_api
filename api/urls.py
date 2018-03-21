# import views from the Application and url rom django.conf.urls
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/users/$', views.UserList.as_view())
]
