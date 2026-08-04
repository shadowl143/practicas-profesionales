from flask import Flask,request, render_template, redirect
from reporte import Reporte
from reportfrom import ReporteForm
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
        fecha_alta= datetime.datetime.now(),
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

    if not data.get("nombre_reporte"):
        return "Campo obligatorio vacío", 400

    nuevo_reporte = Reporte(
        id=id,
        nombre_reporte=data.get("nombre_reporte"),
        descripcion=data.get("descripcion"),
        fecha_alta=datetime.datetime.now(),
        solicitado_por=data.get("solicitado_por"),
        dirigido_a=data.get("dirigido_a"),
        estado=data.get("estado")
    )

    reportes.append(nuevo_reporte)
    id += 1

    return render_template("reportefbv.html", reportes=reportes)

@app.route("/reporte/wtf", methods=["GET", "POST"])
def crear_reporte_wtf():
    global id
    form = ReporteForm()

    if form.validate_on_submit():
        nuevo_reporte = ReporteForm(
            id=id,
            nombre_reporte=form.nombre_reporte.data,
            solicitado_por=form.solicitado_por.data,
            fecha_alta=datetime.datetime.now(),
            dirigido_por=form.dirigido_por.data,
            estado=form.estado.data
        )
        reportes.append(nuevo_reporte)
        id += 1
        return redirect("/reporte/wtf")

    return render_template("reportefbv.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
