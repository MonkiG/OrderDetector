import aiofile
import asyncio

from event_handler import EventHandler
from mic_stream import mic_stream

from amazon_transcribe.client import TranscribeStreamingClient


async def write_chunks(stream):
    # This connects the raw audio chunks generator coming from the microphone
    # and passes them along to the transcription stream.

    async for chunk, status in mic_stream():
        await stream.input_stream.send_audio_event(audio_chunk=chunk)
    await stream.input_stream.end_stream()


async def basic_transcribe():
    # Set up our client with your chosen Region
    client = TranscribeStreamingClient(region="us-east-2")
    # Start transcription to generate async stream
    stream = await client.start_stream_transcription(
        language_code="es-US",
        media_sample_rate_hz=16000,
        media_encoding="pcm",
    )

    # Instantiate our handler and start processing events
    handler = EventHandler(stream.output_stream)
    await asyncio.gather(write_chunks(), handler.handle_events())
