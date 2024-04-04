from langchain_community.llms import Ollama
import speech_recognition as sr
import gtts
from playsound import playsound

def speak(text):
    tts = gtts.gTTS(text)
    tts.save("tmp.mp3")
    playsound("tmp.mp3")


def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Say something!")
        audio = r.listen(source)
    return r.recognize_google(audio)


def chat(text, llm):
    """ Chat with the user
    return the response
    """
    response = llm.invoke(text)
    # remove the '\n' in the middle of the response
    response = response.replace('\n', ' ')
    #
    return response


def main():
    llm = Ollama(model="assistant_tinyllama")
    while True:
        text = listen()
        print(f"User: {text}")
        if text == "exit":
            break
        response = chat(text, llm)
        print(f"Bot: {response}")
        speak(response)


if __name__ == "__main__":
    main()


