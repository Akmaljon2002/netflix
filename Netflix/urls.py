from django.contrib import admin
from django.urls import path
from film.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloAPI.as_view()),
    path('aktyorlar/', AktyorlarAPIView.as_view()),
    path('tariflar/', TariflarAPIView.as_view()),
    path('aktyor/<int:pk>/', AktyorAPIView.as_view()),
    path('tarif/<int:pk>/', TarifDetailView.as_view()),
]
