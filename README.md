## Jarvis – AI Voice Assistant (Python)

Jarvis is a simple AI Voice Assistant built using Python that can recognize voice commands and perform useful tasks such as opening websites and playing music.
The assistant listens for a wake word ("Jarvis") and then executes the requested command.

This project demonstrates the use of speech recognition, text-to-speech, and automation using Python.

## Project Overview

The assistant works using the following workflow:
1. Listens continuously for the wake word **"Jarvis"**
2. Once the wake word is detected, it activates and waits for a command
3. Processes the spoken command
4. Executes the requested action (such as opening a website or playing music)


## Features

* Wake word activation ("Jarvis")
* Voice command recognition
* Text-to-Speech response
* Open popular websites such as:
  * Google
  * YouTube
  * LinkedIn
* Play music using predefined links
* Hands-free interaction


## Technologies Used

* **Python**
* **SpeechRecognition** – for converting speech to text
* **pyttsx3** – for text-to-speech conversion
* **webbrowser module** – for opening websites
* **Microphone input** – for capturing voice commands

