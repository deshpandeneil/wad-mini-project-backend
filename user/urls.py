from django.urls import path, include

from user.serializers import UserSerializer
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    
    path('register/', views.UserCreate.as_view()),
    path('profiles/', views.UserList.as_view()),
    path('profiles/<int:pk>', views.UserDetail.as_view()),
    
    path('add_to_cart/<int:pk>', views.CartAdd.as_view()),
    # path('delete_from_cart/', views.CartDelete),

    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }