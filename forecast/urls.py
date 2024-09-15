from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.requestHelp, name='forecast'),
    path('success_request/', views.requestSuccess, name='success_request'),
]