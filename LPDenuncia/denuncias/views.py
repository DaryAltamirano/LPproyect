from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms
# import forms
def denunciaView(request):
    return render(request,'denuncia.html',{})
class aparecimientoView(CreateView):
    model = models.ReportarAparecimiento
    form_class=forms.ReportarAparecimientoModelForm
    template_name='aparecimiento.html'
    success_url='../denuncias/'

class denuncianteView(CreateView):
    model = models.PersonaDenuncinate
    form_class=forms.PersonaDenuncinateModelForm
    template_name='denunciante.html'
    success_url='../denuncias/'

class avistamientoView(CreateView):
    model = models.UltimoAvistamiento
    form_class=forms.UltimoAvistamientoModelForm
    template_name='avistamiento.html'
    success_url='../denuncias/'

class desaparecidoView(CreateView):
    model = models.PersonaDesaparecida
    form_class=forms.PersonaDesaparecidaModelForm
    template_name='desaparecido.html'
    success_url='../denuncias/'
class sospechosoView(CreateView):
    model = models.Sospecho
    form_class=forms.SospechoModelForm
    template_name='sospechoso.html'
    success_url='../denuncias/'
# Create your views here.
