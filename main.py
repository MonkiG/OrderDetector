import asyncio
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent
import sounddevice
from supabase import supabase  # Asegúrate de que este importe sea correcto
from functools import partial

# Clase para manejar eventos de transcripción
class MyEventHandler(TranscriptResultStreamHandler):
    def __init__(self, output_stream, keywords):
        super().__init__(output_stream)
        self.keywords = [keyword.lower() for keyword in keywords]

    async def handle_transcript_event(self, transcript_event: TranscriptEvent):
        results = transcript_event.transcript.results
        for result in results:
            if result.is_partial:
                continue
            for alt in result.alternatives:
                transcript = alt.transcript.lower()
                if any(keyword in transcript for keyword in self.keywords):
                    print(alt.transcript)
                    await async_insert_order({'transcript': alt.transcript})

# Generador de audio del micrófono
async def mic_stream():
    loop = asyncio.get_event_loop()
    input_queue = asyncio.Queue()

    def callback(indata, frame_count, time_info, status):
        loop.call_soon_threadsafe(input_queue.put_nowait, (bytes(indata), status))

    stream = sounddevice.RawInputStream(
        channels=1, samplerate=16000, callback=callback, blocksize=1024 * 2, dtype="int16")
    with stream:
        while True:
            indata, status = await input_queue.get()
            yield indata, status

# Enviar chunks de audio al servicio de transcripción
async def write_chunks(input_stream):
    async for chunk, status in mic_stream():
        if status:
            print("Error de audio:", status)
        await input_stream.send_audio_event(audio_chunk=chunk)
    await input_stream.end_stream()

# Función asíncrona para insertar datos en Supabase
async def async_insert_order(data):
    loop = asyncio.get_running_loop()
    # Ejecuta la inserción en un thread aparte para no bloquear el loop de asyncio
    response = await loop.run_in_executor(None, partial(supabase.table('pedidos').insert, data).execute)
    if response.error:
        print("Error al insertar:", response.error)
    else:
        print("Inserción exitosa:", response.data)

# Función principal para manejar la transcripción
async def basic_transcribe():
    client = TranscribeStreamingClient(region="us-east-1")
    stream = await client.start_stream_transcription(
        language_code="es-US",
        media_sample_rate_hz=16000,
        media_encoding="pcm"
    )
    handler = MyEventHandler(stream.output_stream, ["dos", "tacos", "mesa", "uno", "tres"])
    audio_stream_task = asyncio.create_task(write_chunks(stream.input_stream))
    handle_events_task = asyncio.create_task(handler.handle_events())
    await asyncio.gather(audio_stream_task, handle_events_task)

# Función main que ejecuta la transcripción
async def main():
    await basic_transcribe()

# Ejecución del script
if __name__ == "__main__":
    asyncio.run(main())



































































