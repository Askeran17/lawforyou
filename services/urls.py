from django.urls import path, include    
from .views import ServiceTemplateView
from . import views

urlpatterns = [
    path("", ServiceTemplateView.as_view(), name="services"),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
