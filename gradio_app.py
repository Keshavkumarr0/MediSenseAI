from dotenv import load_dotenv
load_dotenv()

import os
import logging
import gradio as gr
import speech_recognition as sr

# Import from your modules
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_doctor import text_to_speech, text_to_speech_with_gtts

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# System Prompt
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
What's in this image?. Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Do not add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
Do not say 'In the image I see' but say 'With what I see, I think you have ....'
Don't respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot. 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."""


def process_inputs(audio_filepath, image_filepath):
    """Process audio and image inputs and return results"""
    
    speech_to_text_output = ""
    doctor_response = ""
    audio_file = None
    
    logging.info("🔄 Starting processing...")
    
    # ============================================
    # STEP 1: SPEECH TO TEXT
    # ============================================
    logging.info("📍 Step 1: Converting audio to text...")
    
    if audio_filepath and os.path.exists(audio_filepath) and os.path.getsize(audio_filepath) > 0:
        recognizer = sr.Recognizer()
        
        try:
            logging.info(f"📂 Reading audio file: {audio_filepath}")
            with sr.AudioFile(audio_filepath) as source:
                audio_data = recognizer.record(source)
                speech_to_text_output = recognizer.recognize_google(audio_data, language="en-US")
                logging.info(f"✅ Patient said: {speech_to_text_output}")
        
        except sr.UnknownValueError:
            speech_to_text_output = "⚠️ Could not understand audio. Please speak clearly."
            logging.warning(speech_to_text_output)
        
        except sr.RequestError as e:
            speech_to_text_output = f"❌ Speech recognition error: {e}"
            logging.error(speech_to_text_output)
        
        except Exception as e:
            speech_to_text_output = f"❌ Error during transcription: {e}"
            logging.error(speech_to_text_output)
    
    else:
        speech_to_text_output = "⚠️ No valid audio was recorded or provided."
        logging.warning(speech_to_text_output)
    
    # ============================================
    # STEP 2: IMAGE ANALYSIS WITH GEMINI
    # ============================================
    logging.info("📍 Step 2: Analyzing medical image...")
    
    if image_filepath and os.path.exists(image_filepath):
        try:
            image = encode_image(image_filepath)
            
            if image:
                # Combine system prompt with patient's question
                full_query = system_prompt + "\n\nPatient's Question: " + speech_to_text_output
                
                logging.info("🤖 Calling Gemini AI for analysis...")
                doctor_response = analyze_image_with_query(
                    query=full_query, 
                    encoded_image=image,
                    model="gemini-2.0-flash-exp"
                )
                logging.info(f"✅ Doctor's analysis: {doctor_response[:100]}...")
            
            else:
                doctor_response = "❌ Error: Could not process the image. Please try another image."
                logging.error(doctor_response)
        
        except Exception as e:
            doctor_response = f"❌ Error analyzing image: {e}"
            logging.error(doctor_response)
    
    else:
        doctor_response = "❌ No image provided for me to analyze. Please upload a medical image."
        logging.warning(doctor_response)
    
    # ============================================
    # STEP 3: TEXT TO SPEECH (DOCTOR'S RESPONSE)
    # ============================================
    logging.info("📍 Step 3: Converting doctor's response to speech...")
    
    try:
        output_audio_path = "final_response.mp3"
        
        # Try ElevenLabs first, fallback to gTTS
        audio_file = text_to_speech(
            input_text=doctor_response, 
            use_elevenlabs=True,
            output_filepath=output_audio_path
        )
        
        if audio_file:
            logging.info(f"✅ Audio generated: {audio_file}")
        else:
            logging.warning("⚠️ ElevenLabs failed, trying gTTS...")
            audio_file = text_to_speech_with_gtts(
                input_text=doctor_response,
                output_filepath=output_audio_path
            )
    
    except Exception as e:
        logging.error(f"❌ Text to speech error: {e}")
        audio_file = None
    
    logging.info("✅ Processing complete!\n")
    
    return speech_to_text_output, doctor_response, audio_file


# Create Gradio Interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(
            sources=["microphone"], 
            type="filepath", 
            label="🎤 Speak Your Question"
        ),
        gr.Image(
            type="filepath", 
            label="📷 Upload Medical Image"
        )
    ],
    outputs=[
        gr.Textbox(label="📝 What You Said (Speech to Text)", lines=2),
        gr.Textbox(label="👨‍⚕️ Doctor's Response (Text)", lines=3),
        gr.Audio(label="🔊 Doctor's Voice Response")
    ],
    title="🏥 AI Doctor with Vision and Voice",
    description="Upload a medical image and ask a question about it. The AI doctor will analyze and respond with voice!",
    theme="soft",
    examples=[]
)


# Launch
if __name__ == "__main__":
    # Get port from environment variable (Render provides this)
    port = int(os.environ.get("PORT", 7860))
    
    print("\n" + "="*60)
    print("🚀 Starting AI Doctor Application...")
    print(f"📍 Server running on port: {port}")
    print("="*60 + "\n")
    
    # Launch with Render-compatible settings
    iface.launch(
        server_name="0.0.0.0",  # CRITICAL: Must be 0.0.0.0 for Render
        server_port=port,
        share=False,
        show_error=True,
        debug=True
    )
