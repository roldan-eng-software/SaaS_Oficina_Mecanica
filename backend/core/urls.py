from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ServicoViewSet, AgendamentoViewSet, UserDetailView, TipoServicoViewSet, UserViewSet # Importe UserViewSet
from .views import RegisterView, LogoutView, CookieTokenObtainPairView, CookieTokenRefreshView

router = DefaultRouter()
router.register(r'servicos', ServicoViewSet, basename='servico')
router.register(r'agendamentos', AgendamentoViewSet, basename='agendamento')
router.register(r'tipos-servico', TipoServicoViewSet, basename='tiposervico')
router.register(r'users', UserViewSet, basename='user') # Nova rota para UserViewSet

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('users/me/', UserDetailView.as_view(), name='user_detail'),
]
