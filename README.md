# Malayalam Real-Time Audio to Text Web App

This project is a web application for real-time Malayalam speech recognition and audio recording. It uses the browser's built-in speech recognition (for Malayalam) and records audio, sending both the recognized text and audio files to a Python Flask backend.

## Features

- Real-time Malayalam speech-to-text in your browser (using Chrome/Edge).
- Records and saves audio as `.webm` files.
- Stores recognized Malayalam text in a file.
- Simple web interface for starting/stopping recording and viewing results.

## Requirements

- Python 3.x
- Flask (`pip install flask`)
- A modern browser (Chrome or Edge) with microphone access

## Setup

1. **Clone or Download the Repository**

2. **Install Python Dependencies**
   ```sh
   pip install flask
   ```

3. **Project Structure**
   ```
   mal_desc/
   ├── app.py
   ├── index.html
   ├── recordings/         # Will be created automatically
   └── transcriptions.txt  # Created automatically after first transcription
   ```

4. **Run the Flask App**
   ```sh
   python app.py
   ```

5. **Open the Web App**
   - Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## Usage

1. Click **Start Recording & Listening**.
2. Speak in Malayalam.
3. The recognized text will appear in real time.
4. Click **Stop Recording & Listening** to stop.
5. The recognized text is saved to `transcriptions.txt`.
6. The recorded audio is saved in the `recordings/` folder.

## Notes

- **Speech recognition is performed in the browser** using the Web Speech API (`webkitSpeechRecognition`). No AI model or cloud API is used in the backend.
- **Audio and transcription are sent to the Flask backend** for storage.
- For best results, use Google Chrome or Microsoft Edge.

## Customization

- To process or analyze the audio files, you can extend the backend using libraries like `pydub` or integrate with speech-to-text APIs.
- To change the language, modify the `recognition.lang` property in `index.html`.

## License

This project is for educational purposes.
