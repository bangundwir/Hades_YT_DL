import yt_dlp
import sys
import argparse

# Fungsi hook untuk memproses output dari yt-dlp
def hook(d):
    if d['status'] == 'downloading':
        percentage = d['_percent_str']
        sys.stdout.write(f'\rDownload progress: {percentage}')
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print("\nDownload selesai.")

# Fungsi untuk mendownload video dengan yt-dlp Python module
def download_video(url, download_format):
    # Format download options berdasarkan pilihan pengguna
    format_options = {
        'mp4': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'wav': 'bestaudio[ext=wav]/wav',
        'm4a': 'bestaudio[ext=m4a]/m4a',
        'mp3': 'bestaudio[ext=mp3]/mp3'
    }

    # Opsi untuk yt-dlp
    ydl_opts = {
        'format': format_options[download_format],
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [hook],
    }

    # Mendownload video dengan yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Fungsi utama
def main():
    # Membuat parser argumen
    parser = argparse.ArgumentParser(description='Download videos from YouTube.')
    parser.add_argument('url', nargs='?', help='The YouTube video URL to download.')
    args = parser.parse_args()

    # Jika URL disediakan melalui command line
    if args.url:
        url = args.url
    else:
        # Jika tidak, minta URL dari pengguna
        url = input("Masukkan URL video YouTube: ")

    # Meminta pengguna untuk memilih format download
    download_format = get_download_format()

    # Memanggil fungsi download dengan format yang dipilih
    download_video(url, download_format)

# Meminta pengguna untuk memilih format download
def get_download_format():
    print("Pilih format download:")
    print("1. MP4 (video)")
    print("2. WAV (audio)")
    print("3. M4A (audio)")
    print("4. MP3 (audio)")
    choice = input("Masukkan pilihan (1/2/3/4): ")
    formats = {'1': 'mp4', '2': 'wav', '3': 'm4a', '4': 'mp3'}
    return formats.get(choice, 'mp4')  # Default ke mp4 jika pilihan tidak valid

if __name__ == "__main__":
    main()
