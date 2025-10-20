# 🏥 MediSenseAI - Multimodal AI Medical Consultant with Voice Interface

![MediSenseAI Banner](https://img.shields.io/badge/AI-Medical%20Assistant-blue?style=for-the-badge&logo=robot)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge&logo=google)
![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-purple?style=for-the-badge)

## 📋 Overview

MediSenseAI is an end-to-end AI-powered medical assistant that enables users to upload medical images and ask questions about them using voice input. The system analyzes the images using Google's Gemini multimodal AI and responds with both text and natural voice output powered by ElevenLabs TTS.

### ✨ Key Features

- 🎤 **Voice Input**: Speak your medical questions naturally
- 🖼️ **Image Analysis**: Upload medical images for AI-powered diagnosis
- 🤖 **AI-Powered Responses**: Leverages Google Gemini for accurate medical analysis
- 🔊 **Voice Output**: Hear responses in natural-sounding voice via ElevenLabs
- 📝 **Text Display**: View both transcribed questions and AI responses
- 🎨 **User-Friendly Interface**: Built with Gradio for seamless interaction

## 🏗️ Technical Architecture

The application follows a three-phase workflow:

![Technical Architecture Workflow](https://github.com/Keshavkumarr0/MediSenseAI/blob/main/assets/workflow-diagram.png)

### Phase 1: AI Processing (Google Gemini) 🟡
- User uploads medical image
- Receives transcribed text/user query
- **Multimodal LLM (Gemini)** processes both image and text
- Generates intelligent medical analysis
- Returns comprehensive **LLM Response**

### Phase 2: Speech-to-Text (STT) 🟢
- **Audio Recorder** captures voice input from user
- **Speech to Text (STT AI Model)** converts audio to text
- Transcribed query is sent to Gemini for processing

### Phase 3: Text-to-Speech (ElevenLabs) 🔵
- Receives AI-generated text response
- **Text to Speech (TTS AI Model)** by ElevenLabs converts text to natural speech
- Outputs **audio file** for playback to user

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Gradio |
| **Backend** | Python 3.8+ |
| **AI Model** | Google Gemini (Multimodal LLM) |
| **Speech-to-Text** | AI STT Model |
| **Text-to-Speech** | ElevenLabs API |
| **Image Processing** | PIL/Pillow |

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- ElevenLabs API key

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Keshavkumarr0/MediSenseAI.git
cd MediSenseAI
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up API keys**

Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

4. **Run the application**
```bash
python app.py
```

5. **Access the interface**

Open your browser and navigate to `http://127.0.0.1:7860`

## 💡 How It Works

1. **Upload Medical Image**: Click on the upload section and select a medical image
2. **Speak Your Question**: Click the microphone button and ask about the image (e.g., "Explain the issue in this image")
3. **AI Analysis**: The system processes your question and analyzes the image
4. **Get Response**: Receive both text and voice responses explaining the medical findings

## 📸 Proof of Working

### Live Application Interface

Here's the MediSenseAI application in action, demonstrating the complete voice-to-voice medical consultation workflow:

![Application Demo](https://github.com/Keshavkumarr0/MediSenseAI/blob/main/assets/demo-screenshot.png)

**What's happening in this demo:**

1. **Medical Image Upload** 🖼️: A skin condition image has been uploaded
2. **Voice Question** 🎤: User recorded question - *"Explain the issue of this image"*
3. **Speech-to-Text** 📝: The voice input was transcribed automatically
4. **AI Analysis** 🤖: Doctor's text response shows detailed medical analysis:
   - Diagnosis: Moderate to severe acne vulgaris
   - Observed symptoms: Mix of papules, pustules, possible scarring
   - Recommendations: Gentle skincare routine, topical treatments
   - Advice: Consult dermatologist if condition persists
5. **Voice Response** 🔊: AI response converted to natural voice (26 seconds audio)

### Example Use Case

**User uploads**: Skin condition image showing facial acne  
**User asks** (voice): "Explain the issue of this image"  
**AI responds**: "With what I see, I think you have moderate to severe acne vulgaris, characterized by a mix of papules, pustules, and possibly some scarring. I recommend a gentle skincare routine, topical retinoids or benzoyl peroxide, and consider seeing a dermatologist if the condition doesn't improve, as prescription medications may be needed."

✅ **All features working perfectly**: Voice input ↔️ Image analysis ↔️ Text response ↔️ Voice output

## 🔧 Configuration

The application can be customized by modifying the following parameters:

- **Voice Settings**: Adjust voice speed, pitch, and language in ElevenLabs configuration
- **AI Model**: Switch between different Gemini model versions
- **UI Theme**: Customize Gradio interface theme and layout

## ⚠️ Disclaimer

**Important**: This application is for educational and informational purposes only. It should NOT be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical concerns.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Keshav Kumar**

- GitHub: [@Keshavkumarr0](https://github.com/Keshavkumarr0)

## 🙏 Acknowledgments

- Google Gemini for powerful multimodal AI capabilities
- ElevenLabs for natural text-to-speech technology
- Gradio for the intuitive UI framework

## 📞 Support

If you encounter any issues or have questions, please:
- Open an issue on GitHub
- Check existing issues for solutions
- Contact the maintainer

---

⭐ If you find this project useful, please consider giving it a star!

**Made with ❤️ and AI**
