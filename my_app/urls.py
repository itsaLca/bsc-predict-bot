from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('start/<str:strategy>/<str:ammount>', views.startRobot, name="start"),
    path('stop/', views.stopRobot, name="stop"),
    path('test/', views.test, name="test"),
]
