# AssistantVocal

[![GitHub license](https://img.shields.io/github/license/Jovillios/AssistantVocal.svg)](https://github.com/Jovillios/AssistantVocal/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Jovillios/AssistantVocal.svg)](https://github.com/Jovillios/AssistantVocal/issues)
[![GitHub stars](https://img.shields.io/github/stars/Jovillios/AssistantVocal.svg)](https://github.com/Jovillios/AssistantVocal/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Jovillios/AssistantVocal.svg)](https://github.com/Jovillios/AssistantVocal/network)

AssistantVocal is a simple Python project that acts as a vocal assistant, allowing users to interact with it through speech input and output. This project utilizes several libraries for speech recognition and synthesis, providing a basic conversational interface.

## Installation
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine:
   ```
   git clone https://github.com/Jovillios/AssistantVocal.git
   ```
3. Navigate to the project directory:
   ```
   cd AssistantVocal
   ```
4. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Language Model Setup
1. Obtain the Ollama language model:
   - You can get the Ollama tool by visiting the official website or GitHub repository.
   - For example, to install Ollama via pip:
     ```
     pip install ollama
     ```

2. Create an Ollama model for the assistant:
   - Use the following command to generate the model:
     ```
     ollama create assistant_tinyllama -f ./assistantOllama
     ```
   - This command will create an Ollama model named `assistant_tinyllama` in the `assistantOllama` directory.

## Usage
1. Run the `main.py` script:
   ```
   python main.py
   ```
2. Once the program is running, speak into your microphone when prompted with "Say something!".
3. The assistant will process your speech, provide a response, and speak it back to you.
4. To exit the program, simply say "exit".

## Functionality
- `speak(text)`: Accepts text input and converts it to speech using gTTS (Google Text-to-Speech) library. The synthesized speech is played using the playsound library.
- `listen()`: Utilizes the SpeechRecognition library to listen to the user's speech input via the microphone and returns the recognized text.
- `chat(text, llm)`: Initiates a conversation with the user by sending their input to a language model (llm) for processing and returns the response.
- `main()`: The main function of the program that continuously listens to user input, processes it, and provides responses until the user chooses to exit.

## Note
- This project uses the `Ollama` language model from the `langchain_community` package. Make sure you have the appropriate model installed or replace it with your preferred language model.

Feel free to contribute to this project or customize it according to your needs. If you encounter any issues or have suggestions for improvement, please don't hesitate to open an issue or submit a pull request.
