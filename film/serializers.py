from .models import *
from rest_framework import serializers

class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=30)
    tugilgan_yil = serializers.DateField()
    davlat = serializers.CharField(max_length=30, allow_blank=True)
    jins = serializers.CharField(max_length=30)


class TarifSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=30)
    muddat = serializers.CharField(max_length=30)
    narx = serializers.IntegerField()

