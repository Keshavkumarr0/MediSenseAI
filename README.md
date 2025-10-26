# 🏥 MediSenseAI - Multimodal AI Medical Consultant with Voice Interface

<div align="center">

![MediSenseAI Banner](https://img.shields.io/badge/AI-Medical%20Assistant-blue?style=for-the-badge&logo=robot)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange?style=for-the-badge&logo=google)
![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-purple?style=for-the-badge)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=render)](https://medisenseai-yn0a.onrender.com)

**[🚀 Try Live Demo](https://medisenseai-yn0a.onrender.com)** 

</div>

---

## 📋 Overview 

MediSenseAI is an end-to-end AI-powered medical assistant that enables users to upload medical images and ask questions about them using voice input. The system analyzes the images using Google's Gemini multimodal AI and responds with both text and natural voice output powered by ElevenLabs TTS.

**🔗 Live Application:** [https://medisenseai-yn0a.onrender.com](https://medisenseai-yn0a.onrender.com)

---

## ✨ Key Features

- 🎤 **Voice Input**: Speak your medical questions naturally using built-in microphone
- 🖼️ **Image Analysis**: Upload medical images (X-rays, scans, etc.) for AI-powered analysis
- 🤖 **AI-Powered Responses**: Leverages Google Gemini 2.0 Flash for accurate medical insights
- 🔊 **Voice Output**: Hear responses in natural-sounding voice via ElevenLabs TTS
- 📝 **Text Display**: View both transcribed questions and AI responses in real-time
- 🎨 **User-Friendly Interface**: Built with Gradio for seamless interaction
- 🔒 **Secure**: Environment-based API key management

---
🛠 Workflow Architecture
The application follows a modular, clinical-grade architecture designed for scalability, accuracy, and efficient user interaction. The general workflow consists of the following major components(https://github.com/Keshavkumarr0/MediSenseAI/blob/main/workflow%20architecture.png)

## 🏗️ Technical Architecture

The application follows a three-phase workflow:

### Phase 1: Speech-to-Text (STT) 🟢
1. **Audio Recorder** captures voice input from user
2. **Speech Recognition API** converts audio to text
3. Transcribed query is prepared for processing

### Phase 2: AI Processing (Google Gemini) 🟡
1. User uploads medical image
2. Receives transcribed text/user query
3. **Multimodal LLM (Gemini 2.0 Flash)** processes both image and text simultaneously
4. Generates intelligent medical analysis based on visual + textual context
5. Returns comprehensive **LLM Response**

### Phase 3: Text-to-Speech (ElevenLabs) 🔵
1. Receives AI-generated text response
2. **ElevenLabs TTS API** converts text to natural speech
3. Outputs **audio file** for playback to user

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Gradio 4.44.0 |
| **AI Model** | Google Gemini 2.0 Flash (Experimental) |
| **Speech-to-Text** | Google Speech Recognition API |
| **Text-to-Speech** | ElevenLabs API |
| **Fallback TTS** | gTTS (Google Text-to-Speech) |
| **Backend** | Python 3.8+ |
| **Deployment** | Render |

---

## 🚀 Live Demo

**Access the live application:** [https://medisenseai-yn0a.onrender.com](https://medisenseai-yn0a.onrender.com)

### How to Use:

1. **Upload Medical Image**: Click on image upload area and select a medical scan/X-ray
2. **Record Question**: Click microphone icon and speak your question clearly
3. **Get AI Analysis**: Wait for Gemini AI to analyze the image and question
4. **Listen to Response**: Hear the AI doctor's response in natural voice
5. **Read Text**: Review both your question and the response in text format

  ---

## 🏎️ Performance Report

Check out the latest GTmetrix performance analysis of this AI Doctor application:

![GTmetrix Performance Screenshot](https://github.com/Keshavkumarr0/MediSenseAI/blob/main/Screenshot%20(478).png)

- **GTmetrix Grade:** A (94% Performance, 99% Structure)
- **Largest Contentful Paint (LCP):** 1.6s
- **Total Blocking Time (TBT):** 100ms
- **Cumulative Layout Shift (CLS):** 0

This means the app loads fast, responds instantly, and the layout stays stable for best user experience.

---
 


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

![Application Demo](https://github.com/Keshavkumarr0/MediSenseAI/blob/main/Screenshot%20(399).png)

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


- GitHub: [@Keshavkumarr0](https://github.com/Keshavkumarr0)

## 🙏 Acknowledgments

- Google Gemini for powerful multimodal AI capabilities
- ElevenLabs for natural text-to-speech technology
- Gradio for the intuitive UI framework



**Made with ❤️ and AI**
