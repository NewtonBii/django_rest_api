# import views from the Application
from . import views

urlpatterns = [
    url(r'^api/users/$', views.UserList.as_view())
]
