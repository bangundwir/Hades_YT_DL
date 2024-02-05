# Hades_YT_DL

Hades_YT_DL is a simple Python GUI application for downloading videos and audio from YouTube using `yt_dlp`. It allows users to select the desired format for the download and save it to a specified directory.

## Features

- Download videos in MP4 format.
- Extract audio and download in MP3, M4A, or WAV format.
- Simple and user-friendly interface.
- Download history tracking.
- Light and dark mode themes.

## Installation

To run Hades_YT_DL, you need to have Python installed on your system. If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

Once Python is installed, clone this repository or download the source code:

```bash
git clone https://github.com/your-username/hades_ytDL.git
cd hades_ytDL
```

## Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Usage

To start the application, run the following command in the terminal:

```bash
python hades_ytDL.py
```

```bash
pyinstaller --onefile --windowed --noconfirm --clean --add-data "./campfire.ico;." --icon=./campfire.ico hades_ytDL.py
```


The GUI should launch, allowing you to:

1. Enter the YouTube URL you wish to download.
2. Choose the output format (MP4, MP3, M4A, WAV).
3. Select the download folder.
4. Click the "Download" button to start the download process.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue for any bugs, improvements, or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the `yt_dlp` team for providing the powerful tool for video and audio extraction.
- This project is inspired by the desire to make video downloading simple and accessible to everyone.

