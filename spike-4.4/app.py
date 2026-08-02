from flask import Flask, render_template, request
import datetime, platform

print(datetime.datetime.now().isoformat(), platform.node(), platform.platform())

app = Flask(__name__)

@app.route("/a")
def autoescape_on():
    texto = request.args.get("texto", "")
    return render_template("a_autoescape_on.html", texto=texto)

@app.route("/b")
def autoescape_off():
    texto = request.args.get("texto", "")
    return render_template("b_autoescape_off.html", texto=texto)

@app.route("/c")
def filtro_safe():
    texto = request.args.get("texto", "")
    return render_template("c_filtro_safe.html", texto=texto)

if __name__ == "__main__":
    app.run(debug=True)