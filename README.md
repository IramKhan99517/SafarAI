# 🕋 SafarAI – Intelligent Pilgrim Assistant

SafarAI is an AI-powered assistant designed to support pilgrims during Hajj and Umrah by providing ritual guidance, health alerts, and location-based assistance through an interactive interface.

---

## 🚀 Features

### 🧭 1. Ritual Guidance (RAG-Based)
- Provides step-by-step instructions for rituals like Tawaf and Sa’i
- Uses Retrieval-Augmented Generation (RAG) with text knowledge files

### 🩺 2. Health Assistance
- Detects health risks like heat exhaustion
- Suggests preventive measures

### 📍 3. Location Assistance
- Recommends nearby hospitals, hotels, and emergency services

### 🚨 4. Incident Reporting
- Allows users to report issues such as medical, lost, or crowd incidents

### 💬 5. Interactive Chat UI
- Clean and responsive Streamlit interface
- Supports keyboard (Enter), send button (➡️), and mic trigger (🎤)

---

## 🏗️ Project Structure
hajj-ai-assistance/
│
├── frontend/
│   └── app.py
│
├── agent.py
├── rag.py
├── healthapi.py
├── locationapi.py
│
├── data/
│   ├── tawaf_rituals.txt
│   ├── sai_ritual.txt
│   └── health_precautions.txt
│
├── requirements.txt
└── README.md

## ⚙️ Installation & Run

### 1. Install dependencies
### 2. Run the application

## 🌐 Deployment

This application is designed for deployment using **Streamlit Cloud**.

---

## 🧠 Technologies Used

- Python
- Streamlit (UI)
- RAG (Retrieval-Augmented Generation)
- FastAPI (initial backend design)
- gTTS (optional voice output)

---

## 🎯 Use Cases

- Guidance for pilgrims performing Hajj/Umrah
- Real-time assistance during crowded conditions
- Emergency support and awareness

---

## ✨ Future Enhancements

- Real-time GPS integration
- Multilingual support
- Voice-based interaction (speech recognition)
- Improved UI with animations

---

## 👨‍💻 Developed By

✨ Curated by **Iram Majeed Khan** ✨

---

## 📌 Description

SafarAI aims to enhance the safety, awareness, and experience of pilgrims by combining AI-based knowledge retrieval with real-time assistance.
