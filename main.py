from speech import get_speech_to_text
from utils.serialize_transcription import transcription_to_json
from utils.console import error, warn, log
from services.supabase import save_order


def main():
    while True:
        waiter = ""
        try:
            type, transcription = get_speech_to_text()
            data = transcription_to_json(transcription, type)

            if waiter == "" and not type == "waiter":
                warn(
                    """
                    You should set the waiter before take the order
                    {"set mesero: 'nombre del mesero'"}
                """
                )
                continue
            if type == "order":
                save_order(data, waiter)

            if type == "waiter":
                waiter = data
                log(waiter)

        except Exception as e:
            error(e)


if __name__ == "__main__":
    main()
