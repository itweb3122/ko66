from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('casino/', views.casino, name='casino'),
    path('thethao/', views.thethao, name='thethao'),
    path('xoso/', views.xoso, name='xoso'),
    path('nohu/', views.nohu, name='nohu'),
    path('gamebai/', views.gamebai, name='gamebai'),
    path('banca/', views.banca, name='banca'),
    path('daga/', views.daga, name='daga'),
    path('esport/', views.esport, name='esport'),
    path('khuyenmai/', views.khuyenmai, name='khuyenmai'),
]