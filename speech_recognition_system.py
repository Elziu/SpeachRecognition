import sounddevice as sd
import wave
import speech_recognition as sr
import datetime
import os
import keyboard
import time
import sys
import numpy as np

# Funkcja do nagrywania audio
def record_audio(filename):
    print("Nacisnij 'r', aby rozpoczac nagrywanie...")
    sys.stdout.flush()
    keyboard.wait('r')
    print("Nagrywanie...")
    sys.stdout.flush()
    fs = 44100  # Czestotliwosc probkowania
    channels = 1
    try:
        recording = []
        def callback(indata, frames, time, status):
            if status:
                print(status)
            recording.append(indata.copy())

        with sd.InputStream(samplerate=fs, channels=channels, dtype='int16', callback=callback):
            print("Nacisnij 's', aby zatrzymac nagrywanie...")
            sys.stdout.flush()
            keyboard.wait('s')

        recording = np.concatenate(recording, axis=0)
        
        # Zapisz nagranie do pliku WAV
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(fs)
            wf.writeframes(recording.tobytes())
        
        print(f"Nagranie zakonczone i zapisane jako {filename}")
        sys.stdout.flush()
    except Exception as e:
        print(f"Blad podczas nagrywania: {e}")
        sys.stdout.flush()

# Funkcja do rozpoznawania mowy
def recognize_speech_from_file(filename):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(filename)
    try:
        with audio_file as source:
            audio_data = recognizer.record(source)
        print(f"Dlugosc nagrania: {len(audio_data.frame_data)} bajtow")
        try:
            text = recognizer.recognize_google(audio_data, language='pl-PL')
            print("Rozpoznany tekst:", text)
            sys.stdout.flush()
            save_transcription(filename, text)
        except sr.UnknownValueError:
            print("Nie mozna rozpoznac mowy")
            sys.stdout.flush()
        except sr.RequestError as e:
            print(f"Blad zadania: {e}")
            sys.stdout.flush()
    except Exception as e:
        print(f"Blad podczas rozpoznawania mowy: {e}")
        sys.stdout.flush()

# Funkcja do zapisywania transkrypcji
def save_transcription(audio_filename, text):
    transcription_dir = 'transkrypcje'
    if not os.path.exists(transcription_dir):
        os.makedirs(transcription_dir)
    base_filename = os.path.splitext(os.path.basename(audio_filename))[0]
    transcription_filename = os.path.join(transcription_dir, base_filename + '.txt')
    with open(transcription_filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Transkrypcja zapisana jako {transcription_filename}")
    sys.stdout.flush()

# Glowna funkcja
def main():
    if not os.path.exists('nagrania'):
        os.makedirs('nagrania')
    
    now = datetime.datetime.now()
    filename = f"nagrania/nagranie_{now.strftime('%Y%m%d_%H%M%S')}.wav"
    
    record_audio(filename)
    recognize_speech_from_file(filename)

if __name__ == "__main__":
    main()
