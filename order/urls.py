from django.urls import path
from .views import Checkout, OrderHistory, OrderHistoryDetail

urlpatterns = [
    path('checkout/', Checkout.as_view()),
    path('history/', OrderHistory.as_view()),
    path('history/<int:pk>', OrderHistoryDetail.as_view()),
]