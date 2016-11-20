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
	datos_expediente = {
		"solicitante": "Makoto Hidaka",
		"tipo_solicitud": "2",
		"asunto": "cambio",
		"documentos": "serie de documentos",
		"fecha_creacion": "2016-11-11",
		"fecha_modificacion": "2016-11-11"
	}
	datos_acta = {
		"id_expediente": 1,
		"fecha": "2016-11-11",
		"asunto": "Asunto de prueba",
		"firma": "Firma de prueba"
        }
	self.expediente_creado = self.client.post('/users/expediente_new',datos_expediente,format='json')

	self.usuario_creado = self.client.post('/users/new',usuario,format='json')

	self.registro_creado = self.client.post('/users/acta_new',datos_acta,format='json')
	
	self.expediente_vista = self.client.post('/users/expediente_view',{"correlativo":1},format='json')
	
	self.usuario_vista = self.client.post('/users/view',{"username":"testuser", "user":"user@test.com"},format='json')
	
	self.acta_vista = self.client.post('/users/acta_view',{"id_acta":1},format='json')

    def test_crear_expediente(self):
        self.assertEqual(self.expediente_creado.status_code, status.HTTP_200_OK)

    def test_crear_usuario(self):
	self.assertEqual(self.usuario_creado.status_code, status.HTTP_200_OK)

    def test_crear_registro_acta(self):
	self.assertEqual(self.registro_creado.status_code, status.HTTP_200_OK)
	
	def test_view_expediente(self):
	self.assertEqual(self.expediente_vista.status_code, status.HTTP_200_OK)
	
	def test_view_usuario(self):
	self.assertEqual(self.usuario_vista.status_code, status.HTTP_200_OK)
	
	def test_view_registro_acta(self):
	self.assertEqual(self.acta_vista.status_code, status.HTTP_200_OK)