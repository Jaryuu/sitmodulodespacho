from django.test import TestCase
from models import Acta
from rest_framework import status
from datetime import datetime

class ActaTestCase(TestCase):
    def setUp(self):
        datos_acta = {
			"solicitante": "Makoto Hidaka",
			"tipo_solicitud": "2",
			"asunto": "cambio",
			"documentos": "serie de documentos",
			"fecha_creacion": "2016-11-11",
			"fecha_modificacion": "2016-11-11"
		}
		self.documento_creado = self.client.post('/users/expediente_new',datos_acta,content_type='application/json',auth=('admin','admin123'))


    def test_crear_acta(self):
        self.assertEqual(self.documento_creado.status_code, status.HTTP_201_CREATED)
