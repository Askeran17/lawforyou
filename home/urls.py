from . import views
from django.urls import path, include
from .views import HomeTemplateView

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("accounts/", include("allauth.urls")),
]