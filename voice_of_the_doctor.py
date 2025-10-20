# voice_of_the_doctor.py

import os
import logging
from gtts import gTTS
from elevenlabs import ElevenLabs, save
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if ELEVENLABS_API_KEY:
    logging.info(f"✅ ElevenLabs API key loaded.")
else:
    logging.warning("⚠️ ElevenLabs API key missing in .env file!")


def text_to_speech_with_gtts(input_text, output_filepath="doctor_gtts_output.mp3"):
    """Generate speech using Google TTS (free)."""
    try:
        if not input_text.strip():
            logging.error("❌ Empty text provided to gTTS.")
            return None

        logging.info("🎙️ Generating voice using gTTS...")
        tts = gTTS(text=input_text, lang="en", slow=False)
        tts.save(output_filepath)
        logging.info(f"✅ gTTS voice saved: {output_filepath}")
        return output_filepath

    except Exception as e:
        logging.error(f"❌ gTTS Error: {e}")
        return None


def text_to_speech_with_elevenlabs(input_text, output_filepath="doctor_elevenlabs_output.mp3"):
    """Generate speech using ElevenLabs AI voice (premium)."""
    try:
        if not ELEVENLABS_API_KEY:
            logging.warning("⚠️ ElevenLabs API Key missing — using gTTS fallback.")
            return text_to_speech_with_gtts(input_text, output_filepath)

        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

        logging.info("🎧 Generating voice using ElevenLabs...")
        audio = client.text_to_speech.generate(
            voice_id="pNInz6obpgDQGcFmaJgB",  # Aria voice
            model_id="eleven_turbo_v2",
            text=input_text,
        )

        save(audio, output_filepath)
        logging.info(f"✅ ElevenLabs voice saved: {output_filepath}")
        return output_filepath

    except Exception as e:
        logging.error(f"❌ ElevenLabs Error: {e}")
        logging.info("💡 Falling back to gTTS...")
        return text_to_speech_with_gtts(input_text, output_filepath)


def text_to_speech(input_text, use_elevenlabs=True, output_filepath="doctor_voice.mp3"):
    """Smart function — tries ElevenLabs first, else uses gTTS."""
    if use_elevenlabs and ELEVENLABS_API_KEY:
        return text_to_speech_with_elevenlabs(input_text, output_filepath)
    else:
        return text_to_speech_with_gtts(input_text, output_filepath)


if __name__ == "__main__":
    text = "Hello, this is your AI Doctor. Please follow the prescribed skincare routine carefully."
    result = text_to_speech(text)
    if result:
        print(f"✅ Voice file generated: {result}")
    else:
        print("❌ Voice generation failed!")
