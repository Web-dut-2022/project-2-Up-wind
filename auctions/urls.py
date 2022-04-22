from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("auctions/static/<str:imgurl>", views.static),
    path("listing/<int:listId>", views.listing, name="listing"),
    path("listing/<int:listId>/watch", views.watch, name="watch"),
    path("watch", views.watchlist, name="watchlist")
]
