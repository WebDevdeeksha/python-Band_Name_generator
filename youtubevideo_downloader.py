# video and audio is downloaded in videos and music folder of system by selecting path
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

root = Tk()

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Downloading.....")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)

    # code for mp3 conversion (basically video to audio convert)

    audio_file = video_clip.audio
    audio_file.write_audiofile("audio.mp3")
    audio_file.close()
    shutil.move("audio.mp3", file_path)

    video_clip.close()
    shutil.move(mp4, file_path)
    print("Download Complete")


root.title("Video_Downloader")
canvas = Canvas(root, width=400, height=300)
canvas.pack()

app_label = Label(root, text="Video Downloader", fg="blue", font= ("Arial", 20))
canvas.create_window(200, 20, window=app_label)

url_label = Label(root, text="Enter video URL: ")
url_entry = Entry(root, width=50)

canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

path_label = Label(root, text="Select path to download")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 200, window=path_button)

download_button = Button(root, text="DOWNLOAD", command=download)
canvas.create_window(200, 250, window=download_button)


root.mainloop()