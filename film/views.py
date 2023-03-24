from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *

from .models import *
from .serializers import *

class HelloAPI(APIView):
    def get(self, request):
        content = {
            "xabar":"Salom Dunyo!",
        }
        return Response(content)
    def post(self, request):
        data = request.data
        content = {
            "xabar": "Post so'rov qabul qilindi!",
            "ma'lumot": data
        }
        return Response(content)

class AktyorlarAPIView(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AktyorSerializer(data=request.data)
        if serializer.is_valid():
            Aktyor.objects.create(
                ism = serializer.validated_data.get('ism'),
                davlat = serializer.validated_data.get('davlat'),
                jins = serializer.validated_data.get('jins'),
                tugilgan_yil = serializer.validated_data.get('tugilgan_yil'),
            )
            content = {
                "success":"True",
                "ma'lumot":serializer.data
            }
            return Response(content)
        return Response({"success":"False", "xatolik":serializer.errors})

class AktyorAPIView(APIView):
    def get(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)
    def put(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        ser = AktyorSerializer(aktyor, data=request.data)
        if ser.is_valid():
            aktyor.ism = ser.validated_data.get('ism')
            aktyor.davlat = ser.validated_data.get('davlat')
            aktyor.jins = ser.validated_data.get('jins')
            aktyor.tugilgan_yil = ser.validated_data.get('tugilgan_yil')
            aktyor.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        natija = Aktyor.objects.filter(id=pk).delete()
        if natija[0]:
            return Response({"xabar":"Aktyor ochirildi"})
        return Response({"xabar":"Aktyor yo'q"})


class TariflarAPIView(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializer(tariflar, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TarifSerializer(data=request.data)
        if serializer.is_valid():
            Tarif.objects.create(
                nom = serializer.validated_data.get('nom'),
                narx = serializer.validated_data.get('narx'),
                muddat = serializer.validated_data.get('muddat'),
            )
            content = {
                "success":"True",
                "ma'lumot":serializer.data
            }
            return Response(content)
        return Response({"success": "False", "xatolik": serializer.errors})


class TarifDetailView(APIView):
    def get(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)
    def delete(self, request, pk):
        natija = Tarif.objects.filter(id=pk).delete()
        if natija[0]:
            return Response({"xabar": "Aktyor ochirildi"})
        return Response({"xabar": "Aktyor yo'q"})
    def put(self, request, pk):
        tarif = Tarif.objects.get(id=pk)
        ser = TarifSerializer(tarif, data=request.data)
        if ser.is_valid():
            tarif.nom = ser.validated_data.get('nom')
            tarif.muddat = ser.validated_data.get('muddat')
            tarif.narx = ser.validated_data.get('narx')
            tarif.save()
            return Response(ser.data, status=status.HTTP_202_ACCEPTED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

# class KinolarAPIView(APIView):
#     def get(self, request):
#         kinolar = Kino.objects.all()
#         serializer = KinoSerializer(kinolar, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = KinoCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KinoViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer
    # get, post, patch, delete, retrieve(bittasini get qiladi)
    @action(detail=True)
    # kinolar/3/aktyorlar
    def aktyorlar(self, request, pk):
        kino = Kino.objects.get(id=pk)
        actors = kino.aktyorlar.all()
        serializer = AktyorSerializer(actors, many=True)
        return Response(serializer.data)


class KinoDetailView(APIView):
    def get(self, request, pk):
        kino = Kino.objects.get(id=pk)
        serializer = KinoSerializer(kino)
        return Response(serializer.data)
    def put(self, request, pk):
        kino = Kino.objects.get(id=pk)
        serializer = KinoCreateSerializer(kino, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IzohViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Izoh.objects.all()
    serializer_class = IzohSerilizer

    def get_queryset(self):
        queryset = Izoh.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()

