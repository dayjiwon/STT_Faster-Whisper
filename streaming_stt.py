import sounddevice as sd
import numpy as np
import queue
import threading
import time
import re
from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu", compute_type="int8")

# 예시 명령어
START_KEYWORDS = ["시작", "start", "go"]
STOP_KEYWORDS = ["정지", "stop", "멈춰"]

def classify_command(text):
    clean = text.replace(" ", "").lower()

    if any(k in clean for k in START_KEYWORDS):
        return {"action": "start"}

    if any(k in clean for k in STOP_KEYWORDS):
        return {"action": "stop"}

    return {"action": "unknown"}

def execute_command(cmd):
    if cmd["action"] == "start":
        print("▶ 동작 시작 명령 감지")
    elif cmd["action"] == "stop":
        print("⏹ 동작 중지 명령 감지")
    else:
        print("명령어 해석 불가")

ENERGY_THRESHOLD = 0.03
MIN_VOICE_DURATION = 0.15

audio_q = queue.Queue()
samplerate = 16000

current_voice_buffer = []
voice_start_time = None

def audio_callback(indata, frames, time_info, status):
    audio_q.put(indata.copy())

def stt_worker():
    global current_voice_buffer, voice_start_time
    print("\n실시간 음성 인식 시작\n")

    while True:
        try:
            chunk = audio_q.get(timeout=1)
        except queue.Empty:
            continue

        audio = chunk[:, 0].astype(np.float32)
        energy = np.linalg.norm(audio)

        if energy < ENERGY_THRESHOLD:
            if current_voice_buffer:
                duration = len(current_voice_buffer) / samplerate
                if duration >= MIN_VOICE_DURATION:
                    voice_data = np.array(current_voice_buffer, dtype=np.float32)
                    segments, _ = model.transcribe(voice_data, language="ko", beam_size=1)

                    for seg in segments:
                        text = seg.text.strip()
                        if text:
                            print(f"인식: {text}")
                            cmd = classify_command(text)
                            execute_command(cmd)

            current_voice_buffer = []
            voice_start_time = None
            continue

        if voice_start_time is None:
            voice_start_time = time.time()

        current_voice_buffer.extend(audio.tolist())

stream = sd.InputStream(
    channels=1,
    samplerate=samplerate,
    blocksize=int(samplerate * 0.4),
    callback=audio_callback
)

threading.Thread(target=stt_worker, daemon=True).start()

try:
    with stream:
        while True:
            time.sleep(0.1)
except KeyboardInterrupt:
    print("\n 음성 인식 종료\n")
