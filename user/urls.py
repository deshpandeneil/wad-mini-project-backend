from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', schema_view),
    path('register/', views.UserCreate.as_view()),
    path('profiles/', views.UserList.as_view()),
    path('profiles/<int:pk>', views.UserDetail.as_view()),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]