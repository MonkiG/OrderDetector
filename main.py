from speech import get_speech_to_text
from utils.serialize_transcription import transcription_to_json
from utils.console import error, warn
from services.supabase import save_order


def main():
    while True:
        try:
            type, transcription = get_speech_to_text()
            if type == "order":
                data = transcription_to_json(transcription)
                if not data:
                    continue
                save_order(data)
            else:
                warn("Mesero no seteado todavia, hacerlo")

        except Exception as e:
            error(e)


if __name__ == "__main__":
    main()
