from services.database import conectar

class Membro:

    @staticmethod
    def adicionar(projeto_id, usuario_id):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO projeto_membros
            (projeto_id, usuario_id)
            VALUES (%s, %s)
        """, (
            projeto_id,
            usuario_id
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
            FROM projeto_membros
            WHERE projeto_id = %s
        """, (projeto_id,))

        membros = cur.fetchall()

        cur.close()
        conn.close()

        return membros