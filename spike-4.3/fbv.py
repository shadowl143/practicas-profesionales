from flask import Flask,request, jsonify, render_template
from flask.views import MethodView
from datetime  import datetime
app = Flask("__main__")
reportes = []
id = 1

@app.route("/reporte")
def index():
    return render_template("reportefbv.html", reportes = reportes)

@app.route("/reporte", methods=["POST"])
def crear_reporte():
    global id
    data = request.form
    nuevo_reporte = {
        "id": id,
        "nombre_reporte": data.get("nombre_reporte"),
        "descripcion": data.get("descripcion"),
        "fecha_alta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "solicitado_por": data.get("solicitado_por"),
        "dirigido_a": data.get("dirigido_a"),
        "estado": data.get("estado")
    }
    reportes.append(nuevo_reporte)
    id  += 1
    return render_template("reportefbv.html", reportes = reportes)

if __name__ == "__main__":
    app.run(debug=True)



