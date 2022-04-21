from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("img/<str:imgurl>", views.img, name="image"),
    path("static/<str:imgurl>", views.static, name="static"),
    # path("listing/<int:item>", views.listing, name="listing")
]
