from rest_framework.test import APITestCase, APIClient
from models import *
from rest_framework import status
from datetime import datetime
import base64

class ActaTestCase(APITestCase):
    def setUp(self):
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
	self.documento_creado = client.post('/users/expediente_new',datos_acta,format='json')

    def test_crear_acta(self):
	
        self.assertEqual(self.documento_creado.status_code, status.HTTP_201_CREATED)
