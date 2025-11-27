from rest_framework import viewsets, permissions
from .models import Servico
from .serializers import ServicoSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all().order_by('-id')
    serializer_class = ServicoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        # Permitir que usuários não autenticados criem agendamentos (landing page)
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [perm() for perm in self.permission_classes]


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """Remove (blacklist) um refresh token para efetuar logout.

    Requer o campo JSON `refresh` com o refresh token.
    Requer autenticação (usuário logado).
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Ler refresh token do cookie HttpOnly
        refresh_token = request.COOKIES.get('refresh')
        if not refresh_token:
            # também aceitar no corpo como fallback
            refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'detail': 'Refresh token não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            # remover cookie no cliente
            response = Response({'detail': 'Logout efetuado com sucesso.'}, status=status.HTTP_205_RESET_CONTENT)
            response.delete_cookie('refresh', path='/api/auth/')
            return response
        except Exception:
            response = Response({'detail': 'Token inválido ou expirado.'}, status=status.HTTP_400_BAD_REQUEST)
            response.delete_cookie('refresh', path='/api/auth/')
            return response


class CookieTokenObtainPairView(TokenObtainPairView):
    """Custom TokenObtainPairView que seta o refresh token em cookie HttpOnly e retorna apenas o access no corpo."""

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as exc:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        # serializer.validated_data contém access and refresh
        refresh = data.get('refresh')
        access = data.get('access')
        response = Response({'access': access}, status=status.HTTP_200_OK)
        # set refresh token as HttpOnly cookie
        secure = False
        if not settings.DEBUG:
            secure = True
        response.set_cookie('refresh', refresh, httponly=True, secure=secure, samesite='Lax', path='/api/auth/')
        return response


class CookieTokenRefreshView(TokenRefreshView):
    """TokenRefreshView que lê refresh token do cookie HttpOnly e retorna novo access (e novo refresh quando rotacionado)."""

    def post(self, request, *args, **kwargs):
        # if refresh not in body, try cookie
        if 'refresh' not in request.data or not request.data.get('refresh'):
            cookie_refresh = request.COOKIES.get('refresh')
            if cookie_refresh:
                request.data._mutable = True if hasattr(request.data, '_mutable') else False
                try:
                    request.data['refresh'] = cookie_refresh
                except Exception:
                    # request.data may not support assignment; create new dict
                    request._full_data = request.data.copy()
                    request._full_data['refresh'] = cookie_refresh
        response = super().post(request, *args, **kwargs)
        # if rotation enabled, set cookie to new refresh
        new_refresh = None
        try:
            new_refresh = response.data.get('refresh')
        except Exception:
            new_refresh = None
        if new_refresh:
            secure = False
            if not settings.DEBUG:
                secure = True
            response.set_cookie('refresh', new_refresh, httponly=True, secure=secure, samesite='Lax', path='/api/auth/')
            # optionally remove refresh from response body
            response.data.pop('refresh', None)
        return response
