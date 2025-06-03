from flask import Flask, request, jsonify, send_from_directory
import base64
import os
# from pydub import AudioSegment # Uncomment if you plan to use pydub for audio processing

app = Flask(__name__)

# Define a directory to save recorded audio files
RECORDINGS_DIR = 'recordings'
os.makedirs(RECORDINGS_DIR, exist_ok=True)

@app.route('/')
def index():
    """Serves the index.html file."""
    return send_from_directory('.', 'index.html')

@app.route('/process_transcription', methods=['POST'])
def process_transcription_backend():
    """Receives and processes recognized transcription."""
    try:
        data = request.json
        transcription = data.get('transcription')
        if transcription:
            print("Received Malayalam Text:", transcription)
            # Add your logic to save or process the transcription here
            # For example, saving to a file:
            with open('transcriptions.txt', 'a', encoding='utf-8') as f:
                f.write(transcription + '\n')
            return jsonify({"status": "success", "message": "Transcription processed"}), 200
        else:
            return jsonify({"status": "error", "message": "No transcription data"}), 400
    except Exception as e:
        print(f"Error processing transcription: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/process_audio', methods=['POST'])
def process_audio_backend():
    """Receives and processes audio data."""
    try:
        data = request.json
        audio_data_base64 = data.get('audio_data')
        if audio_data_base64:
            audio_data = base64.b64decode(audio_data_base64)

            # Generate a unique filename
            filename = f"recorded_audio_{len(os.listdir(RECORDINGS_DIR)) + 1}.webm"
            filepath = os.path.join(RECORDINGS_DIR, filename)

            with open(filepath, 'wb') as f:
                f.write(audio_data)

            print(f"Audio data saved to {filepath}")

            # Optional: Use pydub to process the audio
            # try:
            #     audio_segment = AudioSegment.from_file(filepath, format="webm")
            #     # Example: Export to WAV
            #     wav_filepath = filepath.replace('.webm', '.wav')
            #     audio_segment.export(wav_filepath, format="wav")
            #     print(f"Audio converted to WAV: {wav_filepath}")
            # except Exception as e:
            #     print(f"Error processing audio with pydub: {e}")

            return jsonify({"status": "success", "message": "Audio processed and saved", "filename": filename}), 200
        else:
            return jsonify({"status": "error", "message": "No audio data"}), 400
    except Exception as e:
        print(f"Error processing audio data: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Use a different port if 5000 is in use
    app.run(debug=True, port=5000)