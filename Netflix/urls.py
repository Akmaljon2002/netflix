from django.contrib import admin
from django.urls import path, include
from film.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('kinolar', KinoViewSet),
router.register('izohlar', IzohViewSet),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloAPI.as_view()),
    path('aktyorlar/', AktyorlarAPIView.as_view()),
    # path('kinolar/', KinolarAPIView.as_view()),
    path('tariflar/', TariflarAPIView.as_view()),
    path('aktyor/<int:pk>/', AktyorAPIView.as_view()),
    path('tarif/<int:pk>/', TarifDetailView.as_view()),
    path('', include(router.urls)),
    path('get_token/', obtain_auth_token),
    # path('kino/<int:pk>/', KinoDetailView.as_view()),
]
