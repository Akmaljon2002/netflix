from film.models import *
from unittest import TestCase
from rest_framework.test import APIClient


class TestAktyorAPIViews(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_all_actors_view(self):
        natija = self.client.get('/aktyorlar/')
        assert natija.status_code == 200
        assert len(natija.data) == Aktyor.objects.count()
        if len(natija.data) != 0:
            assert natija.data[0]['ism'] == Aktyor.objects.first().ism
            assert natija.data[0]['davlat'] == Aktyor.objects.first().davlat

    def test_actor(self):
        natija = self.client.get('/aktyor/4/')
        assert natija.status_code == 200

        assert natija.data['ism'] == Aktyor.objects.get(id=4).ism

    def test_aktyor_ozgartirish(self):
        aktyor = {
            "ism": "Densel Washington",
            "jins": "Erkak",
            "davlat": "AQSH",
            "tugilgan_yil": "1962-07-29"
        }
        natija = self.client.put('/aktyor/13/', data=aktyor)
        assert natija.status_code == 202
        assert natija.data['ism'] == "Densel Washington"
        assert natija.data['davlat'] == "AQSH"
        assert natija.data['jins'] == "Erkak"



    def test_aktyor_invalid_jins(self):
        aktyor = {
            "ism":"aa",
            "jins":"ayol",
            "davlat":"Angliya",
            "tugilgan_yil":"1995-07-29"
        }
        natija = self.client.post('/aktyorlar/', data=aktyor)
        # assert natija.status_code == 200
        assert natija.data['success'] == 'False'
        assert natija.data["xatolik"]['ism'][0] == "Ism bunaqa kalta bo'lmaydi!"

    # def test_aktyor_qoshish(self):
    #     aktyor = {
    #         "ism": "Emma Watson",
    #         "jins": "Ayol",
    #         "davlat": "Angliya",
    #         "tugilgan_yil": "1995-07-29"
    #     }
    #     natija = self.client.post('/aktyorlar/', data=aktyor)
    #     assert natija.status_code == 200
    #     # assert natija.data['id'] is not None
    #     assert natija.data["ma'lumot"]['ism'] == Aktyor.objects.last().ism
    #     assert natija.data["ma'lumot"]['davlat'] == Aktyor.objects.last().davlat
    #     assert natija.data["ma'lumot"]['jins'] == Aktyor.objects.last().jins

