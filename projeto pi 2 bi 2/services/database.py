import psycopg
from config import Config

def conectar():
    return psycopg.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )

def testar_conexao():
    try:
        conn = conectar()
        conn.close()
        print("Conexão realizada com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar: {e}")