import speech_recognition as sr

def recognize_from_microphone():
    # initialize the recognizer
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_data = r.listen(source, timeout=5)  # Record audio for 5 seconds or until silence is detected

    try:
        print("Recognizing...")
        recognized_text = r.recognize_google(audio_data)
        return recognized_text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def save_text_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(text)

if __name__ == "__main__":
    recognized_text = recognize_from_microphone()
    print("Recognized text:", recognized_text)
    output_filename = "mic_to_text.txt"
    save_text_to_file(recognized_text, output_filename)
    print(f"Recognized text saved to {output_filename}")
