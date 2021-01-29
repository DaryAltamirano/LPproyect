from rest_framework import viewsets
from .models import PersonaDenuncinate,PersonaDesaparecida
from .serializer import PersonaDenuncinateSerializar,PersonaDesaparecidaSerializar

class PersonaDenuncinateViewSet(viewsets.ModelViewSet):
    queryset = PersonaDenuncinate.objects.all()
    serializer_class=PersonaDenuncinateSerializar

class PersonaDesaparecidaViewSet(viewsets.ModelViewSet):
    queryset = PersonaDesaparecida.objects.all()
    serializer_class=PersonaDesaparecidaSerializar
