import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext, ttk, Listbox, Menu
import yt_dlp
import threading
import json
import os
import sys

history_file_path = 'download_history.json'

def show_notification(title, message):
    messagebox.showinfo(title, message)

def on_download_progress(d):
    if d['status'] == 'downloading':
        progress_var.set(f"{d['_percent_str']} - {d['_speed_str']} - ETA {d['_eta_str']}")
    elif d['status'] == 'finished':
        progress_var.set("Download completed")
        terminal_output.insert(tk.END, "\nFinished downloading, now converting ...\n")
        show_notification("Download Complete", "Your download has finished successfully!")
    terminal_output.see(tk.END)

def download_video(url, download_format, output_path):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' if download_format == 'mp4' else 'bestaudio/best',
        'outtmpl': output_path + '/%(title)s.%(ext)s',
        'noplaylist': True,
        'progress_hooks': [on_download_progress],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': download_format,
            'preferredquality': '192',
        }] if download_format != 'mp4' else [],
        'logger': MyLogger(),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        add_to_history(url, output_path)
    except Exception as e:
        terminal_output.insert(tk.END, f"Error: {e}\n")
        terminal_output.see(tk.END)

class MyLogger(object):
    def debug(self, msg):
        if "download" in msg.lower():
            terminal_output.insert(tk.END, msg + '\n')
            terminal_output.see(tk.END)

    def warning(self, msg):
        pass

    def error(self, msg):
        terminal_output.insert(tk.END, msg + '\n')
        terminal_output.see(tk.END)

def start_download():
    url = url_entry.get()
    download_format = format_var.get()
    output_path = folder_entry.get()
    if not url or not output_path:
        messagebox.showwarning("Warning", "Please enter a URL and select an output directory.")
        return
    threading.Thread(target=download_video, args=(url, download_format, output_path), daemon=True).start()

def add_to_history(url, path):
    try:
        history = load_history()
    except FileNotFoundError:
        history = []

    history.append({'url': url, 'path': path})
    with open(history_file_path, 'w') as f:
        json.dump(history, f, indent=4)
    update_history_listbox()

def load_history():
    if not os.path.exists(history_file_path):
        return []
    with open(history_file_path, 'r') as f:
        return json.load(f)

def update_history_listbox():
    history = load_history()
    history_listbox.delete(0, tk.END)
    for item in history:
        history_listbox.insert(tk.END, item['url'])

def toggle_sidebar():
    if sidebar_frame.winfo_ismapped():
        sidebar_frame.pack_forget()
        toggle_button.config(text="Show History")
    else:
        sidebar_frame.pack(side=tk.LEFT, fill='y', padx=10)
        toggle_button.config(text="Hide History")

def copy_history():
    selected = history_listbox.curselection()
    if selected:
        root.clipboard_clear()
        root.clipboard_append(history_listbox.get(selected[0]))

def paste_history():
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, root.clipboard_get())

def delete_history():
    selected = history_listbox.curselection()
    if selected:
        history = load_history()
        history.pop(selected[0])
        with open(history_file_path, 'w') as f:
            json.dump(history, f, indent=4)
        update_history_listbox()

def context_menu(event):
    try:
        context = Menu(root, tearoff=0)
        context.add_command(label="Copy", command=copy_history)
        context.add_command(label="Paste", command=paste_history)
        context.add_command(label="Delete", command=delete_history)
        context.tk_popup(event.x_root, event.y_root)
    finally:
        context.grab_release()

def switch_theme():
    if style.theme_use() == 'clam':
        style.theme_use('default')
        root.configure(background='#F0F0F0')
        style.configure('TFrame', background='#F0F0F0')
        style.configure('TButton', background='#E0E0E0', foreground='black')
        style.configure('TLabel', background='#F0F0F0', foreground='black')
        style.configure('TRadiobutton', background='#F0F0F0', foreground='black')
        style.configure('TCheckbutton', background='#F0F0F0', foreground='black')
        style.configure('TEntry', background='white', foreground='black')
        style.configure('TListbox', background='white', foreground='black')
        style.configure('TScrollbar', background='white', troughcolor='#E0E0E0')
        style.map('TButton', background=[('active', '#D0D0D0'), ('pressed', '#C0C0C0')])
        style.map('TEntry', fieldbackground=[('focus', 'white')])
        style.map('TListbox', background=[('selected', '#C0C0C0')])
        style.map('TScrollbar', background=[('active', '#D0D0D0')])
        switch_button.config(text='Dark Mode')
    else:
        style.theme_use('clam')
        root.configure(background='#333')
        style.configure('TFrame', background='#333')
        style.configure('TButton', background='#555', foreground='white')
        style.configure('TLabel', background='#333', foreground='white')
        style.configure('TRadiobutton', background='#333', foreground='white')
        style.configure('TCheckbutton', background='#333', foreground='white')
        style.configure('TEntry', background='#555', foreground='white')
        style.configure('TListbox', background='#555', foreground='white')
        style.configure('TScrollbar', background='#555', troughcolor='#333')
        style.map('TButton', background=[('active', '#666'), ('pressed', '#333')])
        style.map('TEntry', fieldbackground=[('focus', '#555')])
        style.map('TListbox', background=[('selected', '#333')])
        style.map('TScrollbar', background=[('active', '#666')])
        switch_button.config(text='Light Mode')

# Cek apakah aplikasi dijalankan sebagai file .exe atau sebagai skrip Python
if getattr(sys, 'frozen', False):
    # Jika dijalankan sebagai file .exe
    application_path = sys._MEIPASS
else:
    # Jika dijalankan sebagai skrip Python
    application_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(application_path, 'campfire.ico')

root = tk.Tk()
root.title("Hades_YT_DL")
root.geometry("800x600")
root.resizable(True, True)
root.iconbitmap(icon_path)  # Set the window icon

style = ttk.Style()
style.theme_use('clam')

# Dark mode theme configuration
style.configure('TFrame', background='#333')
style.configure('TButton', background='#555', foreground='white')
style.configure('TLabel', background='#333', foreground='white')
style.configure('TRadiobutton', background='#333', foreground='white')
style.configure('TCheckbutton', background='#333', foreground='white')
style.configure('TEntry', background='#555', foreground='white')
style.configure('TListbox', background='#555', foreground='white')
style.configure('TScrollbar', background='#555', troughcolor='#333')
style.map('TButton', background=[('active', '#666'), ('pressed', '#333')])
style.map('TEntry', fieldbackground=[('focus', '#555')])
style.map('TListbox', background=[('selected', '#333')])
style.map('TScrollbar', background=[('active', '#666')])

root.configure(background='#333')

main_frame = ttk.Frame(root, style='TFrame')
main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

url_label = ttk.Label(main_frame, text="YouTube URL:", style='TLabel')
url_label.pack(pady=5)
url_entry = ttk.Entry(main_frame, width=50)
url_entry.pack(pady=5, fill=tk.X)

folder_label = ttk.Label(main_frame, text="Download Folder:", style='TLabel')
folder_label.pack(pady=5)
folder_entry = ttk.Entry(main_frame, width=50)
folder_entry.pack(pady=5, fill=tk.X)
folder_button = ttk.Button(main_frame, text="Browse", command=lambda: folder_entry.insert(0, filedialog.askdirectory()), style='TButton')
folder_button.pack(pady=5)

format_label = ttk.Label(main_frame, text="Select Format:", style='TLabel')
format_label.pack(pady=5)
format_frame = ttk.Frame(main_frame, style='TFrame')
format_frame.pack(pady=5)
formats = [('MP4', 'mp4'), ('MP3', 'mp3'), ('M4A', 'm4a'), ('WAV', 'wav')]
format_var = tk.StringVar(value='mp3')
for text, value in formats:
    ttk.Radiobutton(format_frame, text=text, variable=format_var, value=value, style='TRadiobutton').pack(side=tk.LEFT)

download_button = ttk.Button(main_frame, text="Download", command=start_download, style='TButton')
download_button.pack(pady=20)

progress_var = tk.StringVar()
progress_label = ttk.Label(main_frame, textvariable=progress_var, style='TLabel')
progress_label.pack(pady=5)

terminal_output = scrolledtext.ScrolledText(main_frame, height=10, bg='#555', fg='white')
terminal_output.pack(pady=5, fill=tk.BOTH, expand=True)

toggle_button = ttk.Button(main_frame, text="Show History", command=toggle_sidebar, style='TButton')
toggle_button.pack(pady=5)

sidebar_frame = ttk.Frame(root, width=200, style='TFrame')
history_label = ttk.Label(sidebar_frame, text="Download History:", style='TLabel')
history_label.pack()
history_listbox = Listbox(sidebar_frame, bg='#555', fg='white')
history_listbox.pack(pady=5, fill=tk.BOTH, expand=True)
history_listbox.bind("<Button-3>", context_menu)

root.update()
sidebar_frame.pack_propagate(False)
sidebar_frame.pack(side=tk.LEFT, fill='y', padx=10)

update_history_listbox()

author_label = ttk.Label(root, text="Author by bangundwir", font=("Arial", 8), background='#333', foreground='white')
author_label.pack(side=tk.BOTTOM, pady=5)

switch_button = ttk.Button(root, text="Light Mode", command=switch_theme, style='TButton')
switch_button.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
