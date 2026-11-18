from datetime import date
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Plataforma, Videojuego


class CatalogoTests(TestCase):
    def setUp(self):
        self.plat = Plataforma.objects.create(nombre='PC')
        self.juego = Videojuego.objects.create(
            plataforma=self.plat, titulo='Hades', precio=Decimal('12990'),
            fecha_lanzamiento=date(2020, 9, 17), disponible=True)
        self.user = User.objects.create_user('profe', password='clave12345')

    def test_lista_publica_y_sin_n_mas_1(self):
        for i in range(5):
            Videojuego.objects.create(
                plataforma=self.plat, titulo=f'J{i}', precio=Decimal('1000'),
                fecha_lanzamiento=date(2021, 1, 1))
        # 1 sola consulta gracias a select_related
        with self.assertNumQueries(1):
            resp = self.client.get(reverse('lista'))
            list(resp.context['videojuegos'])
        self.assertEqual(resp.status_code, 200)

    def test_detalle_404(self):
        self.assertEqual(self.client.get(reverse('detalle', args=[9999])).status_code, 404)

    def test_crear_requiere_login(self):
        resp = self.client.get(reverse('crear'))
        self.assertEqual(resp.status_code, 302)
        self.assertIn('/accounts/login/', resp.url)

    def test_crud_autenticado(self):
        self.client.login(username='profe', password='clave12345')
        resp = self.client.post(reverse('crear'), {
            'titulo': 'Nuevo', 'plataforma': self.plat.pk, 'precio': '9990',
            'fecha_lanzamiento': '2024-01-01', 'disponible': 'on'}, follow=True)
        self.assertContains(resp, 'creado correctamente')
        self.assertEqual(Videojuego.objects.count(), 2)
        resp = self.client.post(reverse('eliminar', args=[self.juego.pk]), follow=True)
        self.assertContains(resp, 'eliminado correctamente')

    def test_botones_ocultos_sin_sesion(self):
        resp = self.client.get(reverse('lista'))
        self.assertNotContains(resp, 'Eliminar')
