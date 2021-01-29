from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .viewsets import PersonaDenuncinateViewSet,PersonaDesaparecidaViewSet
router=routers.SimpleRouter()
router.register('PersonaDenuncinate',PersonaDenuncinateViewSet)
router.register('PersonaDesaparecida',PersonaDesaparecidaViewSet)
urlpatterns = router.urls

# app_name='denuncias'
# urlpatterns = [
#     path('denuncias/', views.denunciaView , name='denuncias'),
#     path('avistamiento/',views.avistamientoView.as_view(),name='avistamiento'),
#     path('aparecimiento/',views.aparecimientoView.as_view(),name='aparecimiento'),
#     path('denunciante/',views.denuncianteView.as_view(),name='denunciante'),
#     path('desaparecimiento/',views.desaparecidoView.as_view(),name='desaparecimiento'),
#     path('sospechoso/',views.sospechosoView.as_view(),name='sospechoso'),
# ]
# urlpatterns += router.urls
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

