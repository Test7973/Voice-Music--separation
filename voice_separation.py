#!/usr/bin/env python3
"""
Voice Separation Script
=========================

This script uses Demucs to separate vocals from an audio file.
It supports both Google Colab (with file uploads) and local execution.

Use Cases:
- Voice separation for karaoke or remixing.
- Instrumental extraction for music production.
- Audio analysis and podcast editing.
"""

import os
import sys
import subprocess
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

from pydub import AudioSegment

# Try to import IPython display functions (available in Colab/Jupyter)
try:
    from IPython.display import Audio, display
except ImportError:
    Audio, display = None, None

# Check if running in Google Colab
try:
    from google.colab import files as colab_files
    COLAB_ENV = True
except ImportError:
    COLAB_ENV = False


def convert_to_wav(input_path, output_path):
    """Convert an audio file to WAV format."""
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format='wav')
        print(f"Successfully converted {input_path} to WAV format")
        return True
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        return False


def separate_audio(input_file):
    """Separate the audio into vocals and accompaniment using Demucs."""
    try:
        print("Starting audio separation...")
        os.makedirs('separated', exist_ok=True)

        # Convert to WAV if needed
        if not input_file.endswith('.wav'):
            wav_file = input_file.rsplit('.', 1)[0] + '.wav'
            if not convert_to_wav(input_file, wav_file):
                return False
            input_file = wav_file

        # Run Demucs separation using subprocess (ensure Demucs is installed)
        result = subprocess.run(['demucs', '--two-stems=vocals', input_file],
                                capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr)
            return False

        return True
    except Exception as e:
        print(f"Error in separation: {str(e)}")
        return False


def main():
    # Obtain input file from Colab file upload or command-line argument
    if COLAB_ENV:
        print("Please upload your MP3 file:")
        uploaded = colab_files.upload()
        if not uploaded:
            print("No file was uploaded.")
            sys.exit()
        input_file = list(uploaded.keys())[0]
    else:
        if len(sys.argv) < 2:
            print("Usage: python voice_separation.py <input_file>")
            sys.exit()
        input_file = sys.argv[1]

    print(f"Processing {input_file}...")

    if separate_audio(input_file):
        try:
            # Define paths based on Demucs output structure
            base_name = os.path.splitext(input_file)[0]
            separated_dir = Path('separated/htdemucs') / base_name
            vocals_path = str(separated_dir / 'vocals.wav')
            no_vocals_path = str(separated_dir / 'no_vocals.wav')

            # Define MP3 output paths
            vocals_mp3 = vocals_path.replace('.wav', '.mp3')
            no_vocals_mp3 = no_vocals_path.replace('.wav', '.mp3')

            if os.path.exists(vocals_path) and os.path.exists(no_vocals_path):
                # Convert separated WAV files to MP3
                vocals = AudioSegment.from_wav(vocals_path)
                no_vocals = AudioSegment.from_wav(no_vocals_path)
                vocals.export(vocals_mp3, format='mp3')
                no_vocals.export(no_vocals_mp3, format='mp3')
                print("\nSeparation completed successfully!")

                if COLAB_ENV and display and Audio:
                    print("\nVocals:")
                    display(Audio(vocals_path))
                    print("\nWithout Vocals:")
                    display(Audio(no_vocals_path))
                    print("\nDownloading separated files...")
                    colab_files.download(vocals_mp3)
                    colab_files.download(no_vocals_mp3)
                else:
                    print(f"Vocals file saved as: {vocals_mp3}")
                    print(f"Non-vocals file saved as: {no_vocals_mp3}")

                # Clean up temporary WAV file if exists
                wav_temp = input_file.replace('.mp3', '.wav')
                if os.path.exists(wav_temp):
                    os.remove(wav_temp)
            else:
                print("Error: Separated files not found. Separation may have failed.")
        except Exception as e:
            print(f"Error in final processing: {str(e)}")
    else:
        print("Audio separation failed. Please try again.")


if __name__ == "__main__":
    main()
