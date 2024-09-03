from django.urls import path, include    
from .views import ServiceTemplateView
from . import views

urlpatterns = [
    path("", ServiceTemplateView.as_view(), name="services"),
    path('add/', views.add_product, name='add_product'),
    path('<slug:url>/', views.product_detail, name='product_detail'),
    path('edit/<slug:url>/', views.edit_product, name='edit_product'),
    path('delete/<slug:url>/', views.delete_product, name='delete_product'),
    path('<slug:url>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:url>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]
