from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highestResolutionStream = streams.get_highest_resolution()
        highestResolutionStream.download(output_path = save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def openFileDialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    
    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

videoURL = input("Please enter a Youtube url: ")
saveDirectory = openFileDialog()

if not saveDirectory:
    print("Invalid save location")
else:
    download_video(videoURL, saveDirectory)
