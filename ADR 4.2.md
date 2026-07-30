# ADR 4.2 — <título de la decisión>
**Contexto:** Es el momento de elegir que framework es el mejor para este proyecto, esta entre flask y django
**Opciones:** A = Flask | B = Django
**Criterio:** Que tan grande es el proyecto? La curva de aprendizaje en cual es mayor? Que puede funcionar mejor en un proyecto escalable?
**Evidencia:** 
1. El numero de lines que se utilizaron para flask fue de
 Lines Words Characters Property
----- ----- ---------- --------
   13  
el tiempo que me tomo hacer el proyecto en flask fue de 10 minutos.

2. El numero de lineas utilizadas con django es:
Lines Words Characters Property
----- ----- ---------- --------
  155  
Su curva de aprendizaje es grande para este proyecto
**Decisión:** Flask para este proyecto es la mejor la opcion ya que al ser un proyecto chico no se necesita mucho esfuerzo, la parte de poder tener mayor estabilidad es una de las cosas 
que en este caso superan a django ya que se trata de una api mas ligera
**Consecuencias:** acepto la flexibilidad que da flask a cambio de todo el ecosistema que maneja django como el orm, formularios, los metodos de administracion que ya vienen con el sistema
**Me haría cambiar de opinión:** Que la aplicacion consumiera altos niveles de picos en usabilidad.