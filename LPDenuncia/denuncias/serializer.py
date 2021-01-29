from rest_framework import serializers
from .models import PersonaDenuncinate,PersonaDesaparecida
class PersonaDenuncinateSerializar(serializers.ModelSerializer):
    class Meta: 
        model =  PersonaDenuncinate
        fields = '__all__'

class PersonaDesaparecidaSerializar(serializers.ModelSerializer):
    class Meta: 
        model =  PersonaDesaparecida
        fields = '__all__'
