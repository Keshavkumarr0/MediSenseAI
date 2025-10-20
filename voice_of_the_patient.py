# patient_voice.py

import os
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def record_audio(file_path="patient_voice.mp3", timeout=15, phrase_time_limit=None):
    """
    Record audio from microphone and save it as MP3 (or WAV fallback).
    Returns audio_data object for transcription.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("🎙️ Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("🔴 Start speaking now...")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("✅ Recording complete!")

            # Convert to MP3
            try:
                wav_data = audio_data.get_wav_data()
                audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
                audio_segment.export(file_path, format="mp3", bitrate="128k")
                logging.info(f"💾 Audio saved to {file_path}")
            except Exception as e:
                logging.warning(f"⚠️ Could not save as MP3: {e}. Saving as WAV instead.")
                fallback_path = file_path.replace(".mp3", ".wav")
                with open(fallback_path, "wb") as f:
                    f.write(audio_data.get_wav_data())
                logging.info(f"💾 Audio saved to {fallback_path}")

            return audio_data

    except sr.UnknownValueError:
        logging.error("❌ Could not understand audio.")
        return None
    except sr.RequestError as e:
        logging.error(f"❌ Microphone error: {e}")
        return None
    except Exception as e:
        logging.error(f"❌ Unexpected error: {e}")
        return None


def transcribe_local(audio_data):
    """Transcribe recorded audio using Google's free STT."""
    recognizer = sr.Recognizer()

    if not audio_data:
        return "❌ No audio data available."

    try:
        logging.info("🧠 Transcribing using Google Speech Recognition...")
        text = recognizer.recognize_google(audio_data, language="en-US")
        logging.info("✅ Transcription complete.")
        return text
    except sr.UnknownValueError:
        return "⚠️ Could not understand audio. Please speak clearly."
    except Exception as e:
        return f"❌ Transcription error: {e}"


if __name__ == "__main__":
    print("🎤 Recording your voice...")
    audio_data = record_audio("patient_voice_test.mp3")

    if audio_data:
        print("⏳ Transcribing...")
        transcription = transcribe_local(audio_data)
        print(f"📝 Transcription: {transcription}")
    else:
        print("❌ Recording failed!")
