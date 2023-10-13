from django.urls import path
from .views import CategoryListAPIView, ServiceListAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    
]
