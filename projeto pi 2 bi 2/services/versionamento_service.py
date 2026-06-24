from models.versao import Versao
from models.solicitacao import Solicitacao


class VersionamentoService:

    @staticmethod
    def criar_versao(
        projeto_id,
        numero,
        descricao
    ):

        Versao.criar(
            projeto_id,
            numero,
            descricao
        )

    @staticmethod
    def solicitar_integracao(
        projeto_id
    ):

        Solicitacao.criar(
            projeto_id
        )

    @staticmethod
    def historico(
        projeto_id
    ):

        return Versao.listar(
            projeto_id
        )

    @staticmethod
    def aprovar_integracao(
        id_solicitacao,
        projeto_id
    ):

        Solicitacao.atualizar_status(
            id_solicitacao,
            "APROVADO"
        )

        versoes = Versao.listar(
            projeto_id
        )

        numero = len(versoes) + 1

        Versao.criar(
            projeto_id,
            f"v{numero}.0",
            "Integração aprovada"
        )