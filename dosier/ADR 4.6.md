# ADR 4.6 — Cuándo aplicar eager loading en listados con relaciones

**Contexto:** Las vistas que listan pedidos acceden al nombre del cliente, generando potencial N+1.
**Opciones:** A = cargar relaciones bajo demanda | B = aplicar eager loading en listados con FK
**Criterio:** Número total de queries ejecutadas para listar 200 pedidos.
**Evidencia:** A = 201 queries (log en spike-4.6/log_sin_eager.txt); B = 1 query (log en spike-4.6/log_con_eager.txt).
**Decisión:** B, porque reduce 201 queries a 1 en el escenario medido.
**Consecuencias:** Se incrementa la complejidad del queryset y puede traer datos innecesarios si no se usan.
**Me haría cambiar de opinión:** Si el dataset fuera pequeño (<10 filas) o la relación no se accediera en el renderizado.