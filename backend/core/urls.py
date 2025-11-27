from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ServicoViewSet
from .views import RegisterView, LogoutView, CookieTokenObtainPairView, CookieTokenRefreshView

router = DefaultRouter()
router.register(r'servicos', ServicoViewSet, basename='servico')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
]
