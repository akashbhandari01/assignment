from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/", views.hello, name="hello"),
    path("users/", views.users_list, name="users"),
    path("users/<int:id>/", views.user_detail, name="user_detail"),
    path("new_user/", views.new_user, name="new_user"),
]
