from services.database import conectar


class Solicitacao:

    @staticmethod
    def criar(projeto_id):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO solicitacoes_integracao
            (
                projeto_id,
                status
            )
            VALUES (%s, %s)
        """, (
            projeto_id,
            "PENDENTE"
        ))

        conn.commit()

        cur.close()
        conn.close()

    @staticmethod
    def listar():

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM solicitacoes_integracao
            ORDER BY id DESC
        """)

        solicitacoes = cur.fetchall()

        cur.close()
        conn.close()

        return solicitacoes

    @staticmethod
    def buscar(id_solicitacao):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM solicitacoes_integracao
            WHERE id = %s
        """, (id_solicitacao,))

        solicitacao = cur.fetchone()

        cur.close()
        conn.close()

        return solicitacao

    @staticmethod
    def atualizar_status(
        id_solicitacao,
        status
    ):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE solicitacoes_integracao
            SET status = %s
            WHERE id = %s
        """, (
            status,
            id_solicitacao
        ))

        conn.commit()

        cur.close()
        conn.close()