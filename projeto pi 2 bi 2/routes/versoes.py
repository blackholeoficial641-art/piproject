from flask import Blueprint
from flask import render_template
from flask import session
from flask import redirect

from models.versao import Versao

versoes_bp = Blueprint(
    "versoes",
    __name__
)

@versoes_bp.route("/versoes/<int:projeto_id>")
def historico(projeto_id):

    if "usuario_id" not in session:
        return redirect("/login")

    versoes = Versao.listar(projeto_id)

    return render_template(
        "versoes/historico.html",
        versoes=versoes,
        projeto_id=projeto_id
    )
@versoes_bp.route("/versao/<int:id_versao>")
def detalhes(id_versao):

    if "usuario_id" not in session:
        return redirect("/login")

    versoes = Versao.listar()

    versao = None

    for v in versoes:

        if v[0] == id_versao:
            versao = v
            break

    return render_template(
        "versoes/detalhes.html",
        versao=versao
    )