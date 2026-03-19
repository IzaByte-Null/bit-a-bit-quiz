from rest_framework import serializers 
from .models import Pergunta, Resposta, Pontuacao, HistoricoBot

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = ['id', 'texto'] 
        

class PerguntaSerializer(serializers.ModelSerializer):
    respostas = RespostaSerializer(many=True, read_only=True) 

    class Meta:
        model = Pergunta
        fields = ['id', 'texto', 'tempo_limite', 'respostas']
 
 


# classe para registrar a pontuaçao / mapear as rotas das perguntas 

class PontuacaoSerializer(serializers.ModelSerializer):
    """
    Serializer para o histórico de pontuações.
    """
    dificuldade_nome = serializers.CharField(source='get_dificuldade_display', read_only=True) 

    class Meta:
        model = Pontuacao
        fields = ['id', 'pontos_totais', 'dificuldade', 'dificuldade_nome', 'data_conclusao']
        read_only_fields = fields


class HistoricoBotSerializer(serializers.ModelSerializer):
    """
    Serializer para monitoramento das interações com a IA.
    Essencial para o Projeto B (Análise de Dados).
    """
    username = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = HistoricoBot
        fields = ['id', 'username', 'pergunta_usuario', 'resposta_bot', 'data_interacao', 'ip_origem']
        read_only_fields = fields