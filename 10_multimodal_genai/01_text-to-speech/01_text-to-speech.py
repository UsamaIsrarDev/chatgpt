from pathlib import Path
from openai import OpenAI

client = OpenAI()

speech_file_path = Path(__path__)

response = client.audio.speech.create(
    model='tts-1',
    voice='alloy',
    input='Today is a wonderfulday to build something people love!',
)

response.stream_to_file(speech_file_path)
