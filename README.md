# Medico Voice 🔊

A FastAPI microservice that turns hospital appointment tickets into natural spoken audio using the ElevenLabs API.

Built as an accessibility feature for [Medico](https://github.com/Muhammadcodes10), a healthcare platform that routes patients in Nigeria to the nearest hospital offering their required treatment.

## Why

Many patients in Nigeria struggle to read appointment details, especially in English. Medico Voice reads a patient's ticket aloud (who, where, when and how much was paid), making digital healthcare more accessible to people with low literacy or visual impairments.

## Demo

[![Medico Voice demo](https://img.youtube.com/vi/BqMIVH5sIdc/0.jpg)](https://youtu.be/BqMIVH5sIdc)

🎬 [Watch the demo on YouTube](https://youtu.be/BqMIVH5sIdc)
## How it works

```
Ticket (JSON)  →  sentence builder  →  ElevenLabs Text-to-Speech  →  MP3 response
```

1. A client (for example, Medico's backend) sends a ticket to `POST /speak-ticket`
2. The ticket is validated with Pydantic
3. A natural sentence is generated from the ticket fields
4. ElevenLabs converts the sentence to speech (`eleven_multilingual_v2`)
5. The audio is returned as `audio/mpeg`

## Tech stack

- Python, FastAPI, Pydantic
- ElevenLabs Python SDK
- python-dotenv for secret management

## Run locally

```bash
git clone https://github.com/Muhammadcodes10/medico-voice.git
cd medico-voice
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
ELEVENLABS_API_KEY=your_api_key_here
```

Start the server:

```bash
uvicorn main:app --reload
```

Interactive API docs: http://127.0.0.1:8000/docs

## Example request

```bash
curl -X POST http://127.0.0.1:8000/speak-ticket \
  -H "Content-Type: application/json" \
  -d '{"patient":"Maryam Ngozi","hospital":"Belam Medical Centre","treatment":"malaria","time":"10:30","amount":12500}' \
  --output ticket.mp3
```

## Security

- The API key is loaded from environment variables and never committed (`.env` is gitignored)
- The ElevenLabs key is restricted to the text-to-speech endpoint, with a usage cap
- Input is validated by Pydantic; invalid requests return `422`

## Roadmap

- [ ] Support Nigerian languages (Hausa, Yoruba, Igbo) where available
- [ ] Integrate with Medico's ticketing flow
- [ ] Add API-key authentication and rate limiting before public deployment
- [ ] Cache audio for repeated tickets to save credits
