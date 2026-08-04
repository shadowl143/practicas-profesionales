# ADR 4.4 — Motores de plantillas y renderizado dinámico de interfaces
**Contexto:** <1 línea: qué problema obliga a decidir>
**Opciones:** A = <script>alert(1)</script> | B = <script>document.body.setAttribute('data-xss','1')</script>
**Criterio:** 
**Evidencia:** <script>alert(1)</script>
**Decisión:** No sepermite usar en formularios solo para generar contenido y sanitizado con alguna herramienta.
**Consecuencias:** se pude inyectar codigo malicioso si no se controla de manera correcta
**Me haría cambiar de opinión:** <qué hallazgo revertiría esta decisión>