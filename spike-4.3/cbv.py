from flask import Flask, request, render_template, redirect, url_for
from flask.views import MethodView
from datetime import datetime

app = Flask(__name__)

reportes = []
contador_id = 1


class ReporteView(MethodView):
    def get(self):
        # Mostrar página con tabla y formulario
        return render_template("reportecbv.html", reportes=reportes)

    def post(self):
        # Crear reporte desde formulario
        global contador_id

        data = request.form

        nuevo_reporte = {
            "id": contador_id,
            "nombre_reporte": data.get("nombre_reporte"),
            "descripcion": data.get("descripcion"),
            "fecha_alta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "solicitado_por": data.get("solicitado_por"),
            "dirigido_a": data.get("dirigido_a"),
            "estado": data.get("estado")
        }

        reportes.append(nuevo_reporte)
        contador_id += 1

        return redirect(url_for("reporte"))

# Registrar vista principal (GET y POST)
reporte_view = ReporteView.as_view("reporte")
app.add_url_rule("/reporte", view_func=reporte_view, methods=["GET", "POST"])


if __name__ == "__main__":
    app.run(debug=True)

