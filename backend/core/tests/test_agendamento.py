from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from core.models import Servico, Agendamento

class AgendamentoTests(APITestCase):
    def setUp(self):
        # Criar usuário e logar
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        login_url = '/api/auth/login/'
        r = self.client.post(login_url, {'username': 'testuser', 'password': 'pass1234'}, format='json')
        self.access_token = r.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        # Criar um serviço para associar
        self.servico = Servico.objects.create(
            cliente='Cliente Teste',
            veiculo='Carro Teste',
            descricao='Troca de oleo'
        )

    def test_crud_agendamento(self):
        url = '/api/agendamentos/'

        # 1. Criar Agendamento
        data = {
            'cliente': 'Cliente Agendado',
            'veiculo': 'Fusca',
            'servico': self.servico.id,
            'data_agendada': '2025-12-01T10:00:00Z',
            'observacoes': 'Verificar freios'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Agendamento.objects.count(), 1)
        agendamento_id = response.data['id']

        # 2. Listar Agendamentos
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # 3. Atualizar Agendamento (Status)
        patch_url = f'{url}{agendamento_id}/'
        response = self.client.patch(patch_url, {'status': 'CONFIRMADO'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'CONFIRMADO')

        # 4. Excluir Agendamento
        response = self.client.delete(patch_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Agendamento.objects.count(), 0)

    def test_create_agendamento_unauthenticated(self):
        self.client.credentials() # Limpar credenciais
        url = '/api/agendamentos/'
        data = {
            'cliente': 'Anonimo',
            'veiculo': 'Carro',
            'servico': self.servico.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
