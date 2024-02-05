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

# Dokumentasi dan Penggunaan `CLi-DL.py`

`CLi-DL.py` adalah skrip Python yang memungkinkan pengguna untuk mendownload video dari YouTube dalam berbagai format audio dan video. Skrip ini menggunakan modul `yt_dlp` untuk melakukan proses download.

## Persyaratan

Sebelum menggunakan skrip ini, pastikan Anda telah menginstal modul `yt_dlp` dengan menjalankan perintah berikut:

```bash
pip install yt-dlp
```



## Penggunaan

Skrip ini dapat digunakan dengan dua cara:

1. **Melalui Command Line (Dengan Argumen URL):**

   Anda dapat langsung memberikan URL video YouTube sebagai argumen ketika menjalankan skrip dari command line. Ini memungkinkan Anda untuk memulai proses download tanpa interaksi tambahan.

   Contoh penggunaan:

   ```bash
   python CLi-DL.py https://www.youtube.com/watch?v=4cdATVG8UbM
   ```

   

   Setelah menjalankan perintah di atas, skrip akan meminta Anda untuk memilih format download yang diinginkan.

2. **Interaktif (Tanpa Argumen URL):**

   Jika Anda tidak menyertakan URL sebagai argumen, skrip akan meminta Anda untuk memasukkan URL dan memilih format download secara interaktif.

   Contoh penggunaan:

   ```bash
   python CLi-DL.py
   ```

   

   Setelah menjalankan perintah di atas, ikuti petunjuk di layar untuk memasukkan URL dan memilih format download.

## Pilihan Format Download

Saat diminta untuk memilih format download, Anda akan diberikan opsi berikut:

```bash
Pilih format download:
1. MP4 (video)
2. WAV (audio)
3. M4A (audio)
4. MP3 (audio)
Masukkan pilihan (1/2/3/4):
```



Masukkan angka yang sesuai dengan format yang Anda inginkan dan tekan Enter.

## Keluar dari Skrip

Setelah proses download selesai, skrip akan berhenti. Jika Anda menjalankan skrip secara interaktif, Anda dapat memulai proses download baru dengan menjalankan skrip lagi.

## Catatan

- Pastikan Anda memiliki hak yang sesuai untuk mendownload konten dari YouTube.
- Kualitas video atau audio yang didownload akan sesuai dengan opsi format yang dipilih dan ketersediaan pada YouTube.
- Proses download akan menampilkan progress bar di command line untuk memberikan informasi tentang proses download.

Dengan mengikuti dokumentasi dan petunjuk penggunaan ini, Anda seharusnya dapat menggunakan `CLi-DL.py` untuk mendownload video dari YouTube dengan mudah.



## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue for any bugs, improvements, or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the `yt_dlp` team for providing the powerful tool for video and audio extraction.
- This project is inspired by the desire to make video downloading simple and accessible to everyone.

