from django.test import TestCase
from quickstart.models import Acta
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
        self.documento_creado = self.client.post('/expediente_create/',datos_acta,format='json')
        

    def test_crear_acta(self):
        self.assertEqual(self.documento_creado.Status, 'OK')