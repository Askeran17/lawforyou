from django.urls import path, include    
from .views import ServiceTemplateView
from . import views

urlpatterns = [
    path("", ServiceTemplateView.as_view(), name="services"),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<slug:slug>/', views.delete_product, name='delete_product'),
]
