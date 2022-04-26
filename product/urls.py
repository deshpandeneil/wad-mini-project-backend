from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view()),
]