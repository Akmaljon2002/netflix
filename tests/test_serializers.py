from film.serializers import *
from unittest import TestCase

class TestAktyorSerializer(TestCase):
    def test_aktyor(self):
        aktyor = {
            "id":3,
            "ism":"Javohir Zokirov",
            "davlat":"O'zbekiston",
            "tugilgan_yil":"1972-09-24",
            "jins":"Erkak"
        }
        serializer = AktyorSerializer(data=aktyor)
        assert serializer.is_valid() == True
        assert serializer.validated_data is not None
        # self.assertTrue(serializer.is_valid() == True) # 2-usul
        # self.assertEqual(serializer.is_valid(), True)   # 3-usul
        malumot = serializer.validated_data
        assert malumot['ism'] == 'Javohir Zokirov'
        assert malumot['davlat'] == "O'zbekiston"
        assert malumot['jins'] == 'Erkak'
        # assert malumot['id'] is not None
        # print(serializer.errors)
        assert True == True
    def test_invalid_ism(self):
        aktyor = {
            "id": 3,
            "ism": "ab",
            "davlat": "O'zbekiston",
            "tugilgan_yil": "1972-09-24",
            "jins": "Erkak"
        }
        serializer = AktyorSerializer(data=aktyor)
        assert serializer.is_valid() == False
        assert serializer.errors['ism'][0] == "Ism bunaqa kalta bo'lmaydi!"
    def test_jins(self):
        aktyor = {
            "id": 3,
            "ism": "Javohir Zokirov",
            "davlat": "O'zbekiston",
            "tugilgan_yil": "1972-09-24",
            "jins": "rkak"
        }
        serializer = AktyorSerializer(data=aktyor)
        assert serializer.is_valid() == False
        assert serializer.errors['jins'][0] == "Jinsni noto'g'ri to'ldirdingiz!"

# class TestKinoSerializer(TestCase):
#     def test_kino(self):
#         kino = {
#             "id":2,
#             "nom":"Sotqin",
#             "janr":"Action",
#             "yil":"2018-05-22",
#             "aktyorlar": []
#         }
#         serializer = KinoCreateSerializer(data=kino)
#         assert serializer.is_valid() == True
#         assert serializer.validated_data['nom'] == "Sotqin"

