
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:username>", views.profile, name="profile"),
    path("following", views.following, name="following"),
    

# API Routes
    path("profileapi/<int:user>", views.profileapi, name="profileapi")

]


