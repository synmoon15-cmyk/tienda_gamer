from datetime import date
from decimal import Decimal

from django.core.management.base import BaseCommand

from catalogo.models import Plataforma, Videojuego


class Command(BaseCommand):
    help = 'Carga 4 plataformas y 12 videojuegos de prueba'

    def handle(self, *args, **options):
        plataformas = {}
        for nombre in ['PlayStation 5', 'Xbox Series X', 'Nintendo Switch', 'PC']:
            plataformas[nombre], _ = Plataforma.objects.get_or_create(nombre=nombre)

        juegos = [
            ('God of War Ragnarok', 'PlayStation 5', '49990', date(2022, 11, 9), True),
            ('Spider-Man 2', 'PlayStation 5', '54990', date(2023, 10, 20), True),
            ('Horizon Forbidden West', 'PlayStation 5', '39990', date(2022, 2, 18), False),
            ('Halo Infinite', 'Xbox Series X', '34990', date(2021, 12, 8), True),
            ('Forza Horizon 5', 'Xbox Series X', '44990', date(2021, 11, 9), True),
            ('Starfield', 'Xbox Series X', '59990', date(2023, 9, 6), True),
            ('Zelda: Tears of the Kingdom', 'Nintendo Switch', '59990', date(2023, 5, 12), True),
            ('Mario Kart 8 Deluxe', 'Nintendo Switch', '49990', date(2017, 4, 28), True),
            ('Animal Crossing: New Horizons', 'Nintendo Switch', '44990', date(2020, 3, 20), False),
            ('Hades', 'PC', '12990', date(2020, 9, 17), True),
            ('Baldur\'s Gate 3', 'PC', '44990', date(2023, 8, 3), True),
            ('Stardew Valley', 'PC', '7990', date(2016, 2, 26), True),
        ]
        creados = 0
        for titulo, plat, precio, fecha, disp in juegos:
            _, nuevo = Videojuego.objects.get_or_create(
                titulo=titulo,
                defaults={'plataforma': plataformas[plat], 'precio': Decimal(precio),
                          'fecha_lanzamiento': fecha, 'disponible': disp})
            creados += nuevo
        self.stdout.write(self.style.SUCCESS(
            f'Listo: {Plataforma.objects.count()} plataformas, {Videojuego.objects.count()} videojuegos ({creados} nuevos).'))
