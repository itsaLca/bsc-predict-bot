from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('metatrader', views.metatrader, name="index"),
    path('calculo/<str:data>', views.calculo, name="view-calculo"),
]
