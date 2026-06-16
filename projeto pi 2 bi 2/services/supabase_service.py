from supabase import create_client

from config import Config


class SupabaseService:

    client = create_client(
        Config.SUPABASE_URL,
        Config.SUPABASE_KEY
    )

    @staticmethod
    def upload(
        nome,
        caminho
    ):

        with open(
            caminho,
            "rb"
        ) as arquivo:

            SupabaseService.client.storage \
                .from_("imagens") \
                .upload(
                    nome,
                    arquivo
                )

        return nome