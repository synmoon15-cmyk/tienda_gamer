# Tienda Gamer — Hito 3 (TI3041)

Django + MySQL. Padre: `Plataforma` (solo Admin). Hijo: `Videojuego` (CRUD con CBVs).

## Puesta en marcha (Windows)
1. En MySQL Workbench abre `database/01_crear_base_de_datos.sql` y ejecútalo (rayo).
2. En `config/settings.py` pon tu clave de MySQL en `DATABASES -> PASSWORD`.
3. En la terminal, dentro de la carpeta del proyecto:
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py cargar_datos
python manage.py runserver
```
4. Abre http://127.0.0.1:8000/ y http://127.0.0.1:8000/admin/
5. En Workbench ejecuta `database/02_verificacion_docente.sql`.

Si `mysqlclient` no instala: `pip install pymysql cryptography` (el proyecto lo usa solo).

Al terminar: `pip freeze > requirements.txt`

## Git (3 commits, uno por bloque)
```
git init
git add .
git commit -m "feat: setup inicial, conexion mysql y modelos relacionales"
git commit -am "feat: ciclo crud completo con cbvs y select_related"
git commit -am "feat: seguridad, autenticacion, feedback y estaticos"
git branch -M main
git remote add origin URL_DE_TU_REPO
git push -u origin main
```
(En sala haz cada commit al terminar su bloque; si todo estuviera junto, igual haz commits separados.)

Pruebas automáticas: `python manage.py test`
