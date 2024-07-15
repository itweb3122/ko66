from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.

def index(request):
    charts = list(Chart.objects.all().values()[:10])
    notice = Notice.objects.all().values()[0]
    service = list(Service.objects.all().values())
    while len(charts) < 10:
        charts += [{'id': len(charts) + 1, 'date': '20240714', 'username': '', 'price': ''}]
    for chart in charts:
        chart['img_url'] = 'static/img/icons/chart/' + str(chart['id']) + '.png'
        chart['username'] = chart['username'][:-4] + '*'*4
    context = {
        'charts': charts,
        'notice': notice['content'],
        'service': service
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def hot(request):
    # hotItems = LobbyItem.objects.filter(lobby='hot').values()
    template = loader.get_template('hot.html')
    return HttpResponse(template.render())

def casino(request):
    # casinoItems = LobbyItem.objects.filter(lobby='casino').values()
    template = loader.get_template('casino.html')
    return HttpResponse(template.render())

def thethao(request):
    # thethaoItems = LobbyItem.objects.filter(lobby='thethao').values()
    template = loader.get_template('thethao.html')
    return HttpResponse(template.render())

def xoso(request):
    # xosoItems = LobbyItem.objects.filter(lobby='xoso').values()
    template = loader.get_template('xoso.html')
    return HttpResponse(template.render())

def nohu(request):
    # nohuItems = LobbyItem.objects.filter(lobby='nohu').values()
    template = loader.get_template('nohu.html')
    return HttpResponse(template.render())

def gamebai(request):
    # gamebaiItems = LobbyItem.objects.filter(lobby='gamebai').values()
    template = loader.get_template('gamebai.html')
    return HttpResponse(template.render())

def banca(request):
    # bancaItems = LobbyItem.objects.filter(lobby='banca').values()
    template = loader.get_template('banca.html')
    return HttpResponse(template.render())

def esport(request):
    # esportItems = LobbyItem.objects.filter(lobby='esport').values()
    template = loader.get_template('esport.html')
    return HttpResponse(template.render())

def daga(request):
    # esportItems = LobbyItem.objects.filter(lobby='esport').values()
    template = loader.get_template('daga.html')
    return HttpResponse(template.render())

def khuyenmai(request):
    # khuyenmaiItems = LobbyItem.objects.filter(lobby='khuyenmai').values()
    template = loader.get_template('khuyenmai.html')
    return HttpResponse(template.render())

def test(request):
    # lobbys = MainLobby.objects.all().values()
    template = loader.get_template('test.html')
    context = {
        'lobbys': lobbys,
    }
    return HttpResponse(template.render(context, request))
