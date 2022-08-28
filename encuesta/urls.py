from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pregunta_id>/', views.detalle, name='detail'),
    path('<int:pregunta_id>/results/', views.resultados, name='results'),
    path('<int:pregunta_id>/vote/', views.votar, name='vote'),
    path('sumar/<int:a>/<int:b>',views.suma),
    path('restar/<int:a>/<int:b>',views.resta),
    path('multiplicar/<int:a>/<int:b>',views.multiplicacion),
   
]
