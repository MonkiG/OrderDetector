from difflib import SequenceMatcher


def product_similarity(transcription_data: str, db_data: str):
    return SequenceMatcher(None, transcription_data, db_data).ratio()
