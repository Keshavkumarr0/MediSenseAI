import os
import base64
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Configure Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


def encode_image(image_path):
    """Load and return PIL Image object"""
    try:
        image = Image.open(image_path)
        print(f"✅ Image loaded: {image_path}")
        return image
    except Exception as e:
        print(f"❌ Error loading image: {e}")
        return None


def analyze_image_with_query(query, encoded_image, model="gemini-2.0-flash-exp"):
    """Analyze image with Gemini AI"""
    try:
        # Create model
        gemini_model = genai.GenerativeModel(model)
        
        # Generate response
        print("🔍 Analyzing image with Gemini...")
        response = gemini_model.generate_content([query, encoded_image])
        
        print("✅ Analysis complete")
        return response.text
    
    except Exception as e:
        error_msg = f"❌ Error in image analysis: {e}"
        print(error_msg)
        return error_msg


# Test function
if __name__ == "__main__":
    image_path = "Clear Focus on Acne Texture.png"
    image = encode_image(image_path)
    
    if image:
        query = """Analyze this skin image and provide:
        1. What conditions or issues you observe
        2. Possible causes
        3. General skincare recommendations
        Note: This is for informational purposes only, not medical advice."""
        
        result = analyze_image_with_query(query, image)
        print("\n--- Analysis Result ---")
        print(result)