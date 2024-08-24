from . import views
from django.urls import path, include

urlpatterns = [
    path("forecast/", views.forecast, name='forecast'),
]