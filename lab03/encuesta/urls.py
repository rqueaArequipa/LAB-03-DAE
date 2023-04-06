from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    path('', views.home, name='home'),
    path('encuesta/', views.index,name='index'),
    path('encuesta/<int:pregunta_id>/',views.detalle,name='detalle'),
    path('encuesta/<int:pregunta_id>/votar',views.votar,name='votar'),
    path('votos/', views.votos, name='votos')
]
