import speech_recognition


def speech_recognizer():
    your_voice = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        your_voice.adjust_for_ambient_noise(source)
        print('Listening... ')
        your_audio = your_voice.listen(source)
        try:
            your_txt = your_voice.recognize_google(your_audio)

            return your_txt
        except speech_recognition.UnknownValueError:
            return "I didn't understand what you said"


if __name__ == '__main__':
    your_txt = speech_recognizer()

    with open('Your_voice.txt', 'w') as file:
        file.write(your_txt)
        print('See your voice in the Your_voice.txt file ')
