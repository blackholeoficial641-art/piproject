from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

from models.usuario import Usuario

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        Usuario.criar(
            nome,
            email,
            senha
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/cadastro.html"
    )


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        senha = request.form["senha"]

        usuario = Usuario.buscar_por_email(
            email
        )

        if usuario and usuario[3] == senha:

            session["usuario_id"] = usuario[0]
            session["usuario_nome"] = usuario[1]

            return redirect("/dashboard")

        return "Login inválido"

    return render_template(
        "auth/login.html"
    )


@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("auth.login")
    )