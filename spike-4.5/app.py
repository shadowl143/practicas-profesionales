from flask import Flask,request, render_template
from reporte import Reporte
from datetime  import datetime
import datetime, platform
contenido = f"{datetime.datetime.now().isoformat()} {platform.node()} {platform.platform()}"
with open("spike-4.3/info.txt", "a", encoding="utf-8") as f:
    f.write(contenido + "\n")

app = Flask("__main__")
reportes = [Reporte]
id = 1

@app.route("/reporte/<name>")
@app.route("/reporte")
def index(name:str = ''):
    if name != '':
        filtrados = [r for r in reportes if r["dirigido_a"] == name]
        return render_template("reportefbv.html", reportes = filtrados)
    return render_template("reportefbv.html", reportes = reportes)

@app.route("/reporte/basico", methods=["POST"])
def crear_reporte_basico():
    global id
    data = request.form

    nuevo_reporte = Reporte(
        id=id,
        nombre_reporte=data.get("nombre_reporte"),
        descripcion=data.get("descripcion"),
        cantidad=data.get("cantidad"),  # sin validar
        fecha_alta=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        solicitado_por=data.get("solicitado_por"),
        dirigido_a=data.get("dirigido_a"),
        estado=data.get("estado")
    )

    reportes.append(nuevo_reporte)
    id += 1
    return render_template("reportefbv.html", reportes=reportes)

@app.route("/reporte/manual", methods=["POST"])
def crear_reporte_manual():
    global id
    data = request.form

    # 1. Validar campos obligatorios
    if not data.get("nombre_reporte"):
        return "Campo obligatorio vacío", 400

    # 2. Validar tipo de dato
    try:
        cantidad = int(data.get("cantidad"))
    except (TypeError, ValueError):
        return "Tipo de dato inválido", 400

    # 3. Validar archivo
    archivo = request.files.get("archivo")
    if archivo and not archivo.filename.endswith(".pdf"):
        return "Formato inválido", 400

    nuevo_reporte = Reporte(
        id=id,
        nombre_reporte=data.get("nombre_reporte"),
        descripcion=data.get("descripcion"),
        cantidad=cantidad,
        fecha_alta=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        solicitado_por=data.get("solicitado_por"),
        dirigido_a=data.get("dirigido_a"),
        estado=data.get("estado")
    )

    reportes.append(nuevo_reporte)
    id += 1

    return render_template("reportefbv.html", reportes=reportes)



if __name__ == "__main__":
    app.run(debug=True)
