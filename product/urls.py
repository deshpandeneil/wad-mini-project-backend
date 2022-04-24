from django.urls import include, path

from rest_framework import routers
from product.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)

urlpatterns = [
   path('', include(router.urls)),
]