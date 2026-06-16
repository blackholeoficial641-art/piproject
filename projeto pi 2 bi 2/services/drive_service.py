from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

from config import Config


class DriveService:

    SCOPES = [
        "https://www.googleapis.com/auth/drive"
    ]

    @staticmethod
    def conectar():

        credenciais = Credentials.from_service_account_file(
            Config.GOOGLE_CREDENTIALS,
            scopes=DriveService.SCOPES
        )

        return build(
            "drive",
            "v3",
            credentials=credenciais
        )

    @staticmethod
    def upload_video(caminho):

        service = DriveService.conectar()

        arquivo = MediaFileUpload(caminho)

        metadata = {
            "name": caminho.split("/")[-1]
        }

        resultado = service.files().create(
            body=metadata,
            media_body=arquivo,
            fields="id"
        ).execute()

        return resultado["id"]