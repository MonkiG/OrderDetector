from speech import get_speech_to_text
from utils.serialize_transcription import transcription_to_json
from utils.console import error, warn, log, success
from services.supabase import save_order
from utils.audio import play_audio
from services.local import save_products_local, save_waiters_local
from utils.similarity import similarity
from utils.json_helpers import get_json


def main():
    save_products_local()
    save_waiters_local()
    waiter = ""
    while True:
        try:
            type, transcription = get_speech_to_text()
            data = transcription_to_json(transcription, type)

            if waiter == "" and not type == "waiter":
                play_audio("error")
                warn(
                    """
                    You should set the waiter before take the order
                    {"set mesero: 'nombre del mesero'"}
                """
                )
                continue

            if type == "order":
                save_order(data, waiter)
                play_audio("ready")

            if type == "waiter":
                waiters = get_json("waiters.json")
                for db_waiter in waiters:
                    warn(f"{data}; {db_waiter["name"]}")
                    ratio = similarity(data, db_waiter["name"])
                    if ratio > 0.5:
                        waiter = data
                        success('Waiter setted correctly')
                        break
                    else:
                        error("Waiter should be in database")

        except Exception as e:
            error(e)


if __name__ == "__main__":
    main()
