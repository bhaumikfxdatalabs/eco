from django.urls import path, include
from users import views


urlpatterns = [
    path("login", views.LoginAPI.as_view()),
    path("logout", views.Logout.as_view()),
    path("registration", views.RegistrationAPI.as_view()),
    # path("user", views.UserAPI.as_view()),
    # path("", views.UserList.as_view()),

]
