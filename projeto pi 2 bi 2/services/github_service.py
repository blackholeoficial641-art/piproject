import requests

from config import Config


class GithubService:

    BASE_URL = "https://api.github.com"

    @staticmethod
    def headers():

        return {
            "Authorization": f"Bearer {Config.GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        }

    @staticmethod
    def usuario():

        resposta = requests.get(
            f"{GithubService.BASE_URL}/user",
            headers=GithubService.headers()
        )

        return resposta.json()

    @staticmethod
    def listar_repositorios():

        resposta = requests.get(
            f"{GithubService.BASE_URL}/user/repos",
            headers=GithubService.headers()
        )

        return resposta.json()

    @staticmethod
    def criar_repositorio(nome):

        dados = {
            "name": nome,
            "private": False
        }

        resposta = requests.post(
            f"{GithubService.BASE_URL}/user/repos",
            headers=GithubService.headers(),
            json=dados
        )

        return resposta.json()