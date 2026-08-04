from flask import Flask, render_template, request, redirect
import jwt
from line_business import jwt_required, usuarios, SECRET
import datetime

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login_jwt():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = usuarios.get(username)

        if user and user["password"] == password and user["activo"]:
            payload = {
                "user": username,
                "rol": user["rol"],
                "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)
            }

            token = jwt.encode(payload, SECRET, algorithm="HS256")

            response = redirect("/dashboard-jwt")
            response.set_cookie("token", token)
            return response

    return render_template("login.html")

@app.route("/dashboard")
@jwt_required
def dashboard_jwt():
    return render_template(
        "dashboard.html",
        user=request.user["user"],
        rol=request.user["rol"]
    )

@app.route("/logout")
def logout_jwt():
    response = redirect("/login")
    response.delete_cookie("token")
    return response



if __name__ == "__main__":
    app.run(debug=True)
