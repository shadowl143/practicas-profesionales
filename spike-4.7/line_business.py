from functools import wraps
from flask import request, redirect
import jwt

SECRET = "mi_clave_super_secreta_de_clavepracticas2026"

usuarios = {
    "julian lara": {"password": "coordinador.2026", "rol": "coordinador", "activo": True},
    "alba contreras": {"password": "usuario.2026", "rol": "usuario", "activo": True},
}

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.cookies.get("token")

        if not token:
            return redirect("/login")

        try:
            data = jwt.decode(token, SECRET, algorithms=["HS256"])
            request.user = data
        except:
            return redirect("/login")

        return f(*args, **kwargs)

    return wrapper
