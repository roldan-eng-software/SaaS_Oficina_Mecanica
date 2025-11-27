from rest_framework.test import APITestCase
from rest_framework import status


class AuthFlowTests(APITestCase):
    def test_register_login_logout_flow(self):
        register_url = '/api/auth/register/'
        login_url = '/api/auth/login/'
        refresh_url = '/api/auth/refresh/'
        logout_url = '/api/auth/logout/'
        servicos_url = '/api/servicos/'

        # 1) Registrar usuário
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'pass1234'}
        r = self.client.post(register_url, data, format='json')
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

        # 2) Obter access (login). Refresh é enviado como cookie HttpOnly.
        r = self.client.post(login_url, {'username': 'testuser', 'password': 'pass1234'}, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertIn('access', r.data)
        access = r.data['access']
        # obter cookie de refresh da resposta
        refresh_cookie = None
        try:
            refresh_cookie = r.cookies.get('refresh').value
        except Exception:
            refresh_cookie = None
        self.assertIsNotNone(refresh_cookie)

        # 3) Acessar endpoint protegido com access token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access)
        r = self.client.get(servicos_url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)

        # 4) Fazer logout (blacklist do refresh) - enviar sem body, cookie será usado
        r = self.client.post(logout_url, format='json')
        self.assertIn(r.status_code, (status.HTTP_205_RESET_CONTENT, status.HTTP_200_OK))

        # 5) Tentar renovar usando o refresh blacklisted (deve falhar)
        r = self.client.post(refresh_url, format='json')
        self.assertIn(r.status_code, (status.HTTP_400_BAD_REQUEST, status.HTTP_401_UNAUTHORIZED))
