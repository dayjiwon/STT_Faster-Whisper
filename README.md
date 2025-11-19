🗣️ STT_Whisper

Real-time Speech-to-Text Command Recognition using Faster-Whisper

🚀 Overview

STT_Whisper is a lightweight real-time speech-to-text command system built on top of Faster-Whisper.
It captures audio from the microphone, detects voice activity using an energy-based VAD, transcribes speech locally, and classifies recognized text into high-level commands (e.g., start/stop) using keyword rules.

This project is fully optimized for CPU-only environments, making it ideal for desktop applications, kiosks, and edge devices without a GPU.

✨ Features

🎤 Real-time microphone streaming using sounddevice

🔇 Energy-based VAD to skip silent sections and reduce computation

⚡ Fast and efficient speech recognition with Faster-Whisper (ONNX runtime)

🔎 Customizable command classification with keyword rules

💻 Runs entirely offline (local inference)

🧩 Easy to integrate into other automation or UI control systems

🛠️ Installation
1) Clone Repository
git clone https://github.com/USER/STT_Whisper.git
cd STT_Whisper

2) Install Dependencies
🔹 Python version check
python3 --version

🔹 Install FFmpeg (Linux)
sudo apt update
sudo apt install -y ffmpeg libportaudio2

🔹 Install Python packages
python3 -m pip install --upgrade pip
pip install onnxruntime onnxruntime-tools
pip install faster-whisper sounddevice scipy


Windows에서는 다음만 설치하면 됩니다:

pip install faster-whisper sounddevice scipy

▶️ Usage

Run the real-time STT program:

python3 stt_whisper.py


You will see something like:

🎤 Real-time speech recognition started
🎯 Recognized: start
▶ Start action triggered

🎯 Recognized: stop
⏹ Stop action triggered


Default commands included:

start, 시작, go

stop, 정지, 멈춰

You can easily modify the keywords inside the source code.

📦 Project Structure
STT_Whisper/
 ├── stt_whisper.py     # Main real-time STT engine
 ├── README.md
 ├── requirements.txt   # (optional)
 └── ...

🧠 Technology Behind This Project
🔹 Whisper

Whisper is an open-source multilingual speech recognition model by OpenAI.
It supports dozens of languages, handles noisy environments well, and works entirely offline.

🔹 Faster-Whisper

A highly optimized implementation of Whisper.

2–4× faster than original Whisper

Lower memory usage

Ideal for CPU-based applications

Uses ONNX Runtime for improved performance

This project uses Whisper small-int8, balancing speed and accuracy.

📌 Future Improvements (Optional Ideas)

Add GUI control panel

Add WebSocket API for external integration

Add wake-word detection (e.g., “Hey Whisper”)

Export recognized text to other services (MQTT, REST API, etc.)

🤝 Contributing

Issues and PRs are welcome! Feel free to improve command rules, VAD logic, or add more features.

📄 License

MIT License.
