from pytube import Playlist
from tkinter import filedialog
# playlist link
p = Playlist(input("enter your playlist link"))
print(f'Downloading: {p.title}')
#choose directory
direc = filedialog.askdirectory()
# loop in playlist videos
for video in p.videos:
    strm = video.streams.get_by_itag(22)
    strm.download(direc)
print("downloaded succesfully")