
# Audio Voice Separation

> *"Sometimes we need voice separation — whether to extract crisp vocals for karaoke, isolate instrumentals for remixes, or analyze audio components for better clarity."*

Welcome to **Audio Voice Separation**, a powerful tool that leverages the state-of-the-art [Demucs](https://github.com/facebookresearch/demucs) model along with Python libraries like `pydub` and `torch` to effortlessly split your audio files into vocals and instrumental tracks.

## Table of Contents

- [Overview](#overview)
- [Use Cases](#use-cases)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Python Script](#python-script)
  - [Jupyter Notebook](#jupyter-notebook)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)

## Overview

Audio Voice Separation is designed for both creative enthusiasts and professionals who need a quick and efficient way to separate vocals from audio tracks. Whether you're a DJ, music producer, podcaster, or researcher, this tool simplifies the process of isolating specific components of an audio file.

## Use Cases

- **Voice Separation:** Create karaoke tracks or remix songs by isolating vocals.
- **Instrumental Extraction:** Remove vocals to produce clean backing tracks.
- **Audio Analysis:** Separate audio components for better clarity in machine learning and signal processing tasks.
- **Podcast Editing:** Isolate and enhance speech from background noise for high-quality podcast production.
- **Music Production:** Remix songs or extract stems for creative mashups and sound design.

## Features

- **Automated Conversion:** Automatically converts input audio files (e.g., MP3) to WAV format for processing.
- **Demucs Integration:** Utilizes Demucs to perform high-quality audio separation.
- **Flexible Usage:** Run the tool in Google Colab or locally on your machine.
- **Easy Playback and Download:** Listen to the separated tracks and download them with ease.
- **Clean-Up Process:** Automatically cleans up temporary files after processing.

## Installation

### Prerequisites

- Python 3.6 or higher
- [pip](https://pip.pypa.io/en/stable/installation/)

### Install Dependencies

Run the following command to install the required libraries:

```bash
pip install -q demucs pydub torch
```

If you are using Google Colab, you can install these dependencies in a notebook cell.

## Usage

### Python Script

The `voice_separation.py` script is designed to run both in Google Colab and on your local machine.

#### Running Locally

```bash
python voice_separation.py path/to/your_audio_file.mp3
```

The script will:
- Convert your file to WAV if necessary.
- Run Demucs to separate the vocals and instrumentals.
- Convert the separated tracks back to MP3.
- Provide options to play and download the output.

#### Running in Google Colab

1. Upload the `voice_separation.ipynb` notebook.
2. Open it in [Google Colab](https://colab.research.google.com).
3. Run each cell sequentially, following the on-screen instructions to upload your audio file.

### Jupyter Notebook

The `voice_separation.ipynb` notebook offers an interactive experience:
- Upload your MP3 file directly from the notebook.
- Execute the cells to process the audio.
- Listen to the separated tracks and download them immediately.

## Code Overview

The project is structured as follows:

- **Conversion to WAV:** Converts the input file into WAV format to ensure compatibility.
- **Audio Separation:** Uses Demucs to split the audio into vocals and instrumentals.
- **Post Processing:** Converts the separated WAV files back into MP3 format.
- **Playback & Download:** Allows you to play the audio in-browser (in Colab/Jupyter) and download the files.
- **Cleanup:** Removes temporary files to keep your workspace tidy.

## Contributing

Contributions are welcome! If you have ideas for improvements or encounter any issues, please open an issue or submit a pull request. Let's build an even better tool together.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Happy audio processing!*
