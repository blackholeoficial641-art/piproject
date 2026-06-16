from services.database import conectar

class Versao:

    @staticmethod
    def criar(
        projeto_id,
        numero,
        descricao
    ):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO versoes
            (
                projeto_id,
                numero,
                descricao
            )
            VALUES (%s, %s, %s)
        """, (
            projeto_id,
            numero,
            descricao
        ))

        conn.commit()

        cur.close()
        conn.close()

    @staticmethod
    def listar(projeto_id):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM versoes
            WHERE projeto_id = %s
            ORDER BY id DESC
        """, (projeto_id,))

        versoes = cur.fetchall()

        cur.close()
        conn.close()

        return versoes