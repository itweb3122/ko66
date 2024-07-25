from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from ko66new import settings
import os
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
    
    context = {
        "img_list": "",
    }
    return HttpResponse(template.render(context, request))

def casino(request):
    img_list = ['AG-truc-tuyen.png', 'BG-truc-tuyen.png', 'DB-truc-tuyen.png', 'DG-truc-tuyen.png', 'EVO-truc-tuyen.png', 'MG-truc-tuyen.png', 'MT-truc-tuyen.png', 'ON-truc-tuyen.png', 'PT-truc-tuyen.png', 'SA-truc-tuyen.png', 'SEXY-truc-tuyen.png', 'TP-truc-tuyen.png', 'VIA-truc-tuyen.png', 'WM-truc-tuyen.png']
    print("=====================================/n")
    print(img_list)
    print("=====================================/n")
    context = {
        "img_list": img_list,
    }
    # img_list1 = os.listdir("/static/img/asset/casino/")
    template = loader.get_template('casino.html')
    return HttpResponse(template.render(context, request))

def thethao(request):
    # thethaoItems = LobbyItem.objects.filter(lobby='thethao').values()
    template = loader.get_template('thethao.html')
    
    context = {
        "img_list": "",
    }
    return HttpResponse(template.render(context, request))

def xoso(request):
    # xosoItems = LobbyItem.objects.filter(lobby='xoso').values()
    template = loader.get_template('xoso.html')
    
    context = {
        "img_list": "",
    }
    return HttpResponse(template.render(context, request))

def nohu(request):
    # nohuItems = LobbyItem.objects.filter(lobby='nohu').values()
    template = loader.get_template('nohu.html')
    
    context = {
        "img_list": "",
    }
    return HttpResponse(template.render(context, request))

def gamebai(request):
    # gamebaiItems = LobbyItem.objects.filter(lobby='gamebai').values()
    template = loader.get_template('gamebai.html')
    
    context = {
        "img_list": "",
    }
    return HttpResponse(template.render(context, request))

def banca(request):
    # bancaItems = LobbyItem.objects.filter(lobby='banca').values()
    template = loader.get_template('banca.html')
    
    context = {
        "img_list": "",
    }
    return HttpResponse(template.render(context, request))

def esport(request):
    # esportItems = LobbyItem.objects.filter(lobby='esport').values()
    template = loader.get_template('esport.html')
    
    context = {
        "img_list": "",
    }
    return HttpResponse(template.render(context, request))

def daga(request):
    # esportItems = LobbyItem.objects.filter(lobby='esport').values()
    template = loader.get_template('daga.html')
    
    context = {
        "img_list": "",
    }
    return HttpResponse(template.render(context, request))

def khuyenmai(request):
    # khuyenmaiItems = LobbyItem.objects.filter(lobby='khuyenmai').values()
    template = loader.get_template('khuyenmai.html')
    
    context = {
        "img_list": "",
    }
    return HttpResponse(template.render(context, request))

def test(request):
    # lobbys = MainLobby.objects.all().values()
    template = loader.get_template('test.html')
    context = {
        'lobbys': lobbys,
    }
    return HttpResponse(template.render(context, request))
