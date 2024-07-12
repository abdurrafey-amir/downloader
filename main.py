from pytube import YouTube
from tkinter import Tk, Label, Entry, Button, messagebox

def download_video():
 url = url_entry.get()
 try:
  obj = YouTube(url)
  streams = obj.streams.get_highest_resolution()
  streams.download()
  messagebox.showinfo("Success", "Video downloaded successfully!")
 except Exception as e:
  messagebox.showerror("Error", str(e))

root = Tk()
root.title("YouTube Video Downloader")

url_label = Label(root, text="Enter YouTube video URL:")
url_label.pack()

url_entry = Entry(root, width=50)
url_entry.pack()

download_button = Button(root, text="Download", command=download_video)
download_button.pack()

root.mainloop()
