from rest_framework import serializers
from .models import *
class PersonaDenuncinateSerializar(serializers.ModelSerializer):
    class Meta: 
        model =  PersonaDenuncinate
        fields = '__all__'

class PersonaDesaparecidaSerializar(serializers.ModelSerializer):
    class Meta: 
        model =  PersonaDesaparecida
        fields = '__all__'
class UltimoAvistamintoSerializar(serializers.ModelSerializer):
    class Meta:
        model = UltimoAvistamiento
        fields='__all__'
class SospechoSerializar(serializers.ModelSerializer):
    class Meta: 
        model = Sospecho
        fields='__all__'
class ReportarAparecimientoSerializar(serializers.ModelSerializer):
     class Meta: 
        model = ReportarAparecimiento
        fields='__all__'