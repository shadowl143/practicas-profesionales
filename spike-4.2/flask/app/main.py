from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(name=None):
    tickets = ["Error del sistema", "problemas con laptop", "No hay tinta en la impresora", "Error mouse", "Error monitor", "Error desarrollo"]
    return render_template("home.html", tickts = tickets[:5])


if __name__ == "__main__":
    app.run(debug = True)