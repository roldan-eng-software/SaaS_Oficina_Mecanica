from rest_framework import serializers
from .models import Servico, Agendamento, Profile, TipoServico # Importar TipoServico
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    telefone = serializers.CharField(source='profile.telefone', required=False, allow_blank=True) # Adicionar telefone

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'telefone', 'is_staff') # Adicionar is_staff

class TipoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServico
        fields = '__all__' # Todos os campos

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        # Explicita os campos para ficar compatível com migrações futuras
        fields = ('id', 'user', 'cliente', 'veiculo', 'descricao', 'telefone', 'email', 'data_agendada', 'status', 'valor', 'concluido')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    telefone = serializers.CharField(required=False, allow_blank=True) # Adicionar telefone

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'telefone') # Incluir telefone

    def create(self, validated_data):
        telefone_data = validated_data.pop('telefone', '') # Remover telefone dos dados do User
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        Profile.objects.create(user=user, telefone=telefone_data) # Criar Profile com telefone
        return user

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ('id', 'cliente', 'veiculo', 'servico', 'data_agendada', 'status', 'observacoes')
