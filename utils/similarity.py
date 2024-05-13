from difflib import SequenceMatcher


def similarity(transcription_data: str, db_data: str):
    return SequenceMatcher(None, transcription_data, db_data).ratio()
