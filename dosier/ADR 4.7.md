# ADR 4.7 — ¿Sesión de servidor o JWT para mi app?
**Contexto:** Mi app tiene rol coordinador que puede desactivar usuarios en cualquier momento.
**Opciones:** A = Sesión de servidor, B = JWT sin infraestructura adicional
**Criterio:** ¿Un usuario desactivado puede seguir accediendo? no
**Evidencia:**  Sesión = NO, JWT = SÍ
**Decisión:** B porque el servidor no guarda nada, cada request se valida con una firma.
**Consecuencias:** Renuncio a la facilidad de sesion y guardar datos en el ervidor.
**Me haría cambiar de opinión:** si es necesario guardar las sesiones en el servidor.