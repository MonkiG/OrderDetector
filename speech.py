import speech_recognition as sr
from utils.audio import play_audio
from utils.console import log, error, success

r = sr.Recognizer()
r.energy_threshold = 4000

waiter = ""


def get_speech_to_text():
    # Sentitive of the recognizer Higher values equeal to less sensitive
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # play audio
        log("Say the order out loud!")

        audio = r.listen(source)

        log("Audio achieved")

        try:
            log("Transcribing audio to text")
            transcription = r.recognize_google(audio, language="es-US")

            if "productos" in transcription:
                success("Transcription completed")
                log("Transcription: ", transcription)
                return ("order", transcription)

            if "mesero" in transcription:
                success("Transcription completed")
                log("Transcription: ", transcription)
                return ("mesero", transcription)

        except Exception as e:
            play_audio("error")
            error("Transcribing error!")
            error(str(e))
