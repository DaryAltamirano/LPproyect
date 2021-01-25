from django.forms import ModelForm
from . import models

class PersonaDenuncinateModelForm(ModelForm):
    class Meta:
        model = models.PersonaDenuncinate
        fields = '__all__'
        
class PersonaDesaparecidaModelForm(ModelForm):
    class Meta:
        model = models.PersonaDesaparecida
        fields = '__all__'
class UltimoAvistamientoModelForm(ModelForm):
    class Meta:
        model = models.UltimoAvistamiento
        fields = '__all__'
class SospechoModelForm(ModelForm):
    class Meta:
        model = models.Sospecho
        fields = '__all__'
class ReportarAparecimientoModelForm(ModelForm):
    class Meta:
        model = models.ReportarAparecimiento
        fields = '__all__'