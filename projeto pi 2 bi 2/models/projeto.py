from services.database import conectar

class Projeto:

    @staticmethod
    def criar(nome, descricao, administrador_id):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO projetos
            (nome, descricao, administrador_id)
            VALUES (%s, %s, %s)
        """, (nome, descricao, administrador_id))

        conn.commit()

        cur.close()
        conn.close()

    @staticmethod
    def listar():

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM projetos
            ORDER BY id DESC
        """)

        projetos = cur.fetchall()

        cur.close()
        conn.close()

        return projetos
    @staticmethod
    def listar_por_usuario(usuario_id):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM projetos
            WHERE administrador_id = %s
            ORDER BY id DESC
        """, (usuario_id,))

        projetos = cur.fetchall()

        cur.close()
        conn.close()

        return projetos