from datetime import datetime
from pydantic import BaseModel

class Reporte(BaseModel):
    id: str
    nombre_reporte: str
    fecha_alta: datetime
    solicitado_por: str
    dirigido_por: str
    estado: str