from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from models.solicitacao import Solicitacao

solicitacoes_bp = Blueprint(
    "solicitacoes",
    __name__
)


@solicitacoes_bp.route("/solicitacoes")
def lista():

    if "usuario_id" not in session:
        return redirect("/login")

    solicitacoes = Solicitacao.listar()

    return render_template(
        "solicitacoes/lista.html",
        solicitacoes=solicitacoes
    )

@solicitacoes_bp.route(
    "/solicitacao/<int:id_solicitacao>",
    methods=["GET", "POST"]
)
def aprovar(id_solicitacao):

    if "usuario_id" not in session:
        return redirect("/login")

    solicitacao = Solicitacao.buscar(
        id_solicitacao
    )

    if request.method == "POST":

    status = request.form["status"]

    if status == "APROVADO":

        from services.versionamento_service import VersionamentoService

        VersionamentoService.aprovar_integracao(
            id_solicitacao,
            solicitacao[1]
        )

    else:

        Solicitacao.atualizar_status(
            id_solicitacao,
            status
        )

    return redirect("/solicitacoes")