from flask import Flask

from routes.auth import auth_bp
from routes.projetos import projetos_bp
from routes.versoes import versoes_bp
from routes.github import github_bp
from routes.drive import drive_bp
from routes.imagens import imagens_bp
from routes.solicitacoes import solicitacoes_bp

app = Flask(__name__)

app.config.from_object("config.Config")

app.register_blueprint(auth_bp)
app.register_blueprint(projetos_bp)
app.register_blueprint(versoes_bp)
app.register_blueprint(github_bp)
app.register_blueprint(drive_bp)
app.register_blueprint(imagens_bp)
app.register_blueprint(solicitacoes_bp)

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