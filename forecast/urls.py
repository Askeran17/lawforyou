from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.requestHelp, name='forecast'),
    path('s/', views.requestSuccess, name='success_request'),
]