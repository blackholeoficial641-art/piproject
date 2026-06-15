from services.database import conectar

class Usuario:

    @staticmethod
    def criar(nome, email, senha):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO usuarios
            (nome, email, senha)
            VALUES (%s, %s, %s)
        """, (nome, email, senha))

        conn.commit()

        cur.close()
        conn.close()

    @staticmethod
    def buscar_por_email(email):

        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM usuarios
            WHERE email = %s
        """, (email,))

        usuario = cur.fetchone()

        cur.close()
        conn.close()

        return usuario