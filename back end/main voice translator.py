import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def translate_and_speak(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    translated_text = translation.text

    print(f"Translated Text ({target_language}): {translated_text}")

    # Speak the translated text
    tts = gTTS(translated_text, lang=target_language, slow=False)
    tts.save("translated_audio.mp3")
    os.system("start translated_audio.mp3")

def main():
    user_input = speech_to_text()

    if user_input:
        target_language = input("Enter the target language code (e.g., 'es' for Spanish): ").lower()
        translate_and_speak(user_input, target_language)

if __name__ == "__main__":
    main()