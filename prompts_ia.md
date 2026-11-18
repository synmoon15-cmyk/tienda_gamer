# Bitácora de uso de IA — Hito 3 (TI3041)

**Asistente utilizado:** Claude (Anthropic)

## Prompt 1 (Front-End)
- **Rol:** Eres un desarrollador front-end experto en Bootstrap 5 y plantillas DTL de Django.
- **Tarea:** Convierte el listado de videojuegos en una grilla de tarjetas responsivas con badge de disponibilidad.
- **Contexto:** Proyecto Django con base.html; la vista entrega la variable `videojuegos` con `plataforma` cargada con select_related.
- **Formato:** Solo el código de la plantilla lista.html, con comentarios breves.

## Prompt 2 (Depuración)
- **Rol:** Eres un depurador experto en Django y control de acceso.
- **Tarea:** Explica por qué mi CreateView deja entrar a usuarios sin sesión.
- **Contexto:** Mi clase estaba definida como `class X(CreateView, LoginRequiredMixin)`.
- **Formato:** Causa en máximo 2 líneas y el código corregido.

**Resultado:** LoginRequiredMixin debe ir a la izquierda por el MRO.
