from django.contrib.auth.models import User
from django.db import models


class Aktyor(models.Model):
    ism = models.CharField(max_length=30)
    davlat = models.CharField(max_length=30, blank=True)
    tugilgan_yil = models.DateField()
    jins = models.CharField(max_length=7)
    def __str__(self):
        return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=50)
    janr = models.CharField(max_length=50)
    yil = models.DateField()
    aktyorlar = models.ManyToManyField(Aktyor)
    def __str__(self):
        return self.nom

class Tarif(models.Model):
    nom = models.CharField(max_length=30)
    muddat = models.CharField(max_length=30)
    narx = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.nom

class Izoh(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    matn = models.TextField()
    def __str__(self):
        return f"{self.user}({self.kino})"
