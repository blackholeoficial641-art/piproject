from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from models.projeto import Projeto

projetos_bp = Blueprint(
    "projetos",
    __name__
)

@projetos_bp.route("/dashboard")
def dashboard():

    if "usuario_id" not in session:
        return redirect("/login")

    projetos = Projeto.listar_por_usuario(
    session["usuario_id"]
)
    return render_template(
        "projetos/dashboard.html",
        projetos=projetos,
        usuario=session["usuario_nome"]
    )

@projetos_bp.route("/criar-projeto", methods=["GET", "POST"])
def criar_projeto():

    if "usuario_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        nome = request.form["nome"]
        descricao = request.form["descricao"]

        Projeto.criar(
            nome,
            descricao
        )

        return redirect("/dashboard")

    return render_template(
        "projetos/criar_projeto.html"
    )