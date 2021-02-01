from rest_framework import viewsets
from .models import *
from .serializer import *

class PersonaDenuncinateViewSet(viewsets.ModelViewSet):
    queryset = PersonaDenuncinate.objects.all()
    serializer_class=PersonaDenuncinateSerializar

class PersonaDesaparecidaViewSet(viewsets.ModelViewSet):
    queryset = PersonaDesaparecida.objects.all()
    serializer_class=PersonaDesaparecidaSerializar 

class UltimoAvistamientoViewSet(viewsets.ModelViewSet):
    queryset=UltimoAvistamiento.objects.all()
    serializer_class=UltimoAvistamintoSerializar

class SospechoViewSet(viewsets.ModelViewSet):
    queryset = Sospecho.objects.all()
    serializer_class=SospechoSerializar

class ReportarAparecimientoViewSet(viewsets.ModelViewSet):
    queryset = ReportarAparecimiento.objects.all()
    serializer_class = ReportarAparecimientoSerializar