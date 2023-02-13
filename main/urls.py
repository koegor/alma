from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('spec', views.spec, name='spec'),
    path('quest', views.quest, name='quest'),
    path('result', views.result, name='result'),
]
