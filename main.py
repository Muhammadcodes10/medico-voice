import os

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from fastapi import FastAPI, Response
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError("ELEVENLABS_API_KEY is missing. Check your .env file")

client = ElevenLabs(api_key=api_key)
app = FastAPI()


class Ticket(BaseModel):
    patient: str
    hospital: str
    treatment: str
    time: str
    amount: int


def ticket_to_speech(ticket: Ticket) -> str:
    return (
        f"Hello {ticket.patient}. Your {ticket.treatment} appointment at "
        f"{ticket.hospital} is at {ticket.time}. "
        f"Amount paid: {ticket.amount:,} naira."
    )


@app.get("/")
def root():
    return {"message": "Medico Voice is running"}


@app.post("/speak-ticket")
def speak_ticket(ticket: Ticket):
    text = ticket_to_speech(ticket)                     # 1. build the sentence
    audio = client.text_to_speech.convert(              # 2. ask ElevenLabs for speech
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        text=text,
        output_format="mp3_44100_128",
    )
    audio_bytes = b"".join(audio)                       # 3. glue the chunks together
    return Response(content=audio_bytes, media_type="audio/mpeg")  # 4. send it back as MP3