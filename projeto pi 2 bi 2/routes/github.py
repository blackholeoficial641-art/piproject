from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from services.github_service import GithubService

github_bp = Blueprint(
    "github",
    __name__
)


@github_bp.route("/github")
def github():

    if "usuario_id" not in session:
        return redirect("/login")

    repositorios = GithubService.listar_repositorios()

    return render_template(
        "github/repositorios.html",
        repositorios=repositorios
    )


@github_bp.route("/github/criar", methods=["POST"])
def criar_repo():

    if "usuario_id" not in session:
        return redirect("/login")

    nome = request.form["nome"]

    GithubService.criar_repositorio(nome)

    return redirect("/github")