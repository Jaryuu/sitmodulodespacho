from django.test import TestCase
from models import Acta
from rest_framework import status
from datetime import datetime

class ActaTestCase(TestCase):
    def setUp(self):
        datos_acta = {
                'id_acta':1,
                'id_expediente':1,
                'fecha':datetime.now(),
                'asunto':'asunto',
                'firma':'firma'
        }
		
        self.documento_creado = self.client.post('/users/expediente_new/',datos_acta,format='json',auth=('situser','toor1234'))


    def test_crear_acta(self):
        self.assertEqual(self.documento_creado.status_code, status.HTTP_201_CREATED)
