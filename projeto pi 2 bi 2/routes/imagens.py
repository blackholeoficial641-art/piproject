from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from services.supabase_service import SupabaseService

imagens_bp = Blueprint(
    "imagens",
    __name__
)


@imagens_bp.route("/imagens")
def imagens():

    if "usuario_id" not in session:
        return redirect("/login")

    return render_template(
        "imagens/upload.html"
    )


@imagens_bp.route("/imagens/upload", methods=["POST"])
def upload():

    imagem = request.files["imagem"]

    caminho = f"uploads/imagens/{imagem.filename}"

    imagem.save(caminho)

    SupabaseService.upload(
        imagem.filename,
        caminho
    )

    return redirect("/imagens")