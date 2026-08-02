from flask import Flask, render_template, request
import datetime, platform
contenido = f"{datetime.datetime.now().isoformat()} {platform.node()} {platform.platform()}"
with open("spike-4.3/info.txt", "a", encoding="utf-8") as f:
    f.write(contenido + "\n")


app = Flask(__name__)

@app.route("/a")
def autoescape_on():
    texto = request.args.get("texto", "")
    return render_template("autoescape_on.html", texto=texto)

@app.route("/b")
def autoescape_off():
    texto = request.args.get("texto", "")
    return render_template("autoescape_off.html", texto=texto)

@app.route("/c")
def filtro_safe():
    texto = request.args.get("texto", "")
    return render_template("filtro_safe.html", texto=texto)

if __name__ == "__main__":
    app.run(debug=True)