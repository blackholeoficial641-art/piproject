from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from services.drive_service import DriveService

drive_bp = Blueprint(
    "drive",
    __name__
)


@drive_bp.route("/drive")
def drive():

    if "usuario_id" not in session:
        return redirect("/login")

    return render_template(
        "drive/upload.html"
    )


@drive_bp.route("/drive/upload", methods=["POST"])
def upload():

    if "usuario_id" not in session:
        return redirect("/login")

    video = request.files["video"]

    caminho = f"uploads/videos/{video.filename}"

    video.save(caminho)

    DriveService.upload_video(caminho)

    return redirect("/drive")