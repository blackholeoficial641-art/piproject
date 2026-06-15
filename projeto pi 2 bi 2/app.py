from flask import Flask
from routes.auth import auth_bp
from routes.projetos import projetos_bp

app = Flask(__name__)

app.config.from_object('config.Config')

app.register_blueprint(auth_bp)
app.register_blueprint(projetos_bp)

@app.route("/")
def home():
    return """
    <h1>Sistema de Versionamento Colaborativo</h1>

    <a href='/login'>Login</a><br>
    <a href='/cadastro'>Cadastro</a><br>
    <a href='/dashboard'>Dashboard</a>
    """

if __name__ == "__main__":
    app.run(debug=True)