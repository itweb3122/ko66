from django.db import models

# Create your models here.
class BrandInfo(models.Model):
    brandName = models.CharField(max_length=100)
    heroLogo = models.ImageField(null=True)
    favicon = models.ImageField(null=True)
    title = models.CharField(max_length=200)
    decription = models.CharField(max_length=200)

class MainLobby(models.Model):
    lobbyId = models.IntegerField()
    lobbyName = models.CharField(max_length=100)
    icons = models.ImageField(null=True)
    date =  models.DateTimeField(auto_now_add=True)
    
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Banner(models.Model):
    img = models.ImageField()
    isDeleted = models.IntegerField()

class LobbyItem(models.Model):
    lobbyName = models.CharField(max_length=20)
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()

class Notice(models.Model):
    content = models.TextField()

class Chart(models.Model):
    date = models.IntegerField()
    username = models.CharField(max_length=100)
    price = models.FloatField(max_length=255)

class TopGame(models.Model):
    nameItem = models.CharField(max_length=40)
    lobbyId = models.IntegerField()
    order = models.IntegerField()

class HotGame(models.Model):
    nameItem = models.CharField(max_length=40)
    lobbyId = models.IntegerField()
    order = models.IntegerField()

class Service(models.Model):
    serviceName = models.CharField(max_length=20)
    describe = models.TextField()

class HotLobby(models.Model):
    lobbyId = models.IntegerField()
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()
    order = models.IntegerField()

class CasinoLobby(models.Model):
    lobbyId = models.IntegerField()
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()
    order = models.IntegerField()

class TheThaoLobby(models.Model):
    lobbyId = models.IntegerField()
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()
    order = models.IntegerField()

class XosoLobby(models.Model):
    lobbyId = models.IntegerField()
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()
    order = models.IntegerField()

class NohuLobby(models.Model):
    lobbyId = models.IntegerField()
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()
    order = models.IntegerField()

class GamebaiLobby(models.Model):
    lobbyId = models.IntegerField()
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()
    order = models.IntegerField()

class BancaLobby(models.Model):
    lobbyId = models.IntegerField()
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()
    order = models.IntegerField()

class DagaLobby(models.Model):
    lobbyId = models.IntegerField()
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()
    order = models.IntegerField()

class EsportLobby(models.Model):
    lobbyId = models.IntegerField()
    img = models.ImageField(null=True)
    nameItem = models.CharField(max_length=40)
    isDeleted = models.IntegerField()
    isActive = models.IntegerField()
    order = models.IntegerField()
