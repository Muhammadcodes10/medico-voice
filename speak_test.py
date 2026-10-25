import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    raise ValueError("ELEVENLABS_API_KEY is missing. Check your .env file")


ticket = {
    "patient": "Amina",
    "hospital": "Maitama District Hospital",
    "treatment": "malaria",
    "time": "10:30",
    "amount": 12500,
}

def ticket_to_speech(ticket: dict) -> str:
    return (f"Hello {ticket["patient"]}. Your {ticket["treatment"]} appointment at {ticket["hospital"]} is at {ticket["time"]}. Amount paid: {ticket["amount"]:,} naira")



ticket_to_speech(ticket)

client = ElevenLabs(api_key=api_key)

audio = client.text_to_speech.convert(
    voice_id="JBFqnCBsd6RMkjVDRZzb",       # a default voice ("George")
    model_id="eleven_multilingual_v2",     # supports many languages
    text=ticket_to_speech(ticket),
    output_format="mp3_44100_128",
)

with open("ticket.mp3", "wb") as f:     # "wb" = write binary
    for chunk in audio:
        f.write(chunk)