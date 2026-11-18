-- Consultas de verificacion que pedira el docente (ejecutar DESPUES de migrate + cargar_datos)
USE tienda_gamer;

-- 1. Conteo de padres (minimo 4)
SELECT COUNT(*) AS total_padres FROM catalogo_plataforma;

-- 2. Conteo de hijos (minimo 10)
SELECT COUNT(*) AS total_hijos FROM catalogo_videojuego;

-- 3. Integridad relacional con INNER JOIN
SELECT h.id, h.titulo, p.nombre AS clasificacion
FROM catalogo_videojuego h
INNER JOIN catalogo_plataforma p ON h.plataforma_id = p.id;
