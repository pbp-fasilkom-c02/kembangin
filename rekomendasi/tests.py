from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from rekomendasi.views import *
from rekomendasi.models import Rekomendasi

# Create your tests here.
class RekomendasiTest(TestCase):

    def setUp(self):
        self.dummy_rekomendasi = {
            'data': '{"nama_barang": "test", "harga_barang": "test", "deskripsi": "test", "url": "test", "gambar": "test"}'
            
        }

        self.credentials = {
            'username': 'testrekomendasi',
            'password': 'akucantikbanget'
        }
        self.user = get_user_model().objects.create_user(
            username= self.credentials['username'],
            email = '',
            password= self.credentials['password']
        )
        self.user.save()

    def test_show_rekomendasi(self):
        c = Client()
        c.login(**self.credentials)

        response = c.get('/rekomendasi/')

        self.assertEqual(response.status_code, 200)

    def test_show_json(self):
        c = Client()
        c.login(**self.credentials)
        response = c.get('/rekomendasi/json/')

        self.assertEqual(response.status_code, 200)

    def test_add_rekomendasi(self):
        c = Client()
        c.login(**self.credentials)
        c.get('/rekomendasi/')

        response = c.post('/rekomendasi/add/', self.dummy_rekomendasi)
        
        self.assertEqual(response.status_code, 200)
    
    def test_get_add_rekomendasi(self):
        c = Client()
        c.login(**self.credentials)
        response = c.get('/rekomendasi/add/')
        
        self.assertEqual(response.status_code, 200)
        
