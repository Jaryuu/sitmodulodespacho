from rest_framework.test import APITestCase, APIClient
from models import *
from rest_framework import status
from datetime import datetime
import base64

class ActaTestCase(APITestCase):
    def setUp(self):
        usuario = {
			"username": "testuser",
			"password": "test1234",
			"first_name": "Test",
			"last_name": "User",
			"email": "user@test.com",
		}
		datos_acta = {
			"solicitante": "Makoto Hidaka",
			"tipo_solicitud": "2",
			"asunto": "cambio",
			"documentos": "serie de documentos",
			"fecha_creacion": "2016-11-11",
			"fecha_modificacion": "2016-11-11"
		}
		datos_acta = {
			"solicitante": "Makoto Hidaka",
			"tipo_solicitud": "2",
			"asunto": "cambio",
			"documentos": "serie de documentos",
			"fecha_creacion": "2016-11-11",
			"fecha_modificacion": "2016-11-11"
		}
	persona = AuthUser(username='admin',password='admin123',is_superuser=1,is_staff=1,is_active=1)
	persona.save()
		
	client = APIClient()
	client.login(username='admin',password='admin123')
	self.expediente_creado = self.client.post('/users/expediente_new',datos_acta,content_type='application/json',auth=('admin','admin123'))
		
	self.usuario_creado = self.client.post('/users/new',usuario,content_type='application/json',auth=('admin','admin123'))

    def test_crear_acta(self):
        self.assertEqual(self.expediente_creado.status_code, status.HTTP_200_OK)

	def test_crear_usuario(self):
		self.assertEqual(self.usuario_creado.status_code, status.HTTP_200_OK)