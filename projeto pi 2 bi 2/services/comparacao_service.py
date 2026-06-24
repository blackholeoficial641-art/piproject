import os


class ComparacaoService:

    @staticmethod
    def comparar(
        pasta_a,
        pasta_b
    ):

        arquivos_a = set(
            os.listdir(
                pasta_a
            )
        )

        arquivos_b = set(
            os.listdir(
                pasta_b
            )
        )

        adicionados = list(
            arquivos_b - arquivos_a
        )

        removidos = list(
            arquivos_a - arquivos_b
        )

        modificados = list(
            arquivos_a.intersection(
                arquivos_b
            )
        )

        return {
            "adicionados": adicionados,
            "removidos": removidos,
            "modificados": modificados
        }