from pytube import YouTube
import os 


youtube_downloader = YouTube('https://youtu.be/T2BQG_8CFHI?si=a9o-CLhbg0Uso01F')
movie = youtube_downloader.streams.get_highest_resolution()
movie.download()

#Download to format mp3
song = youtube_downloader.streams.filter(only_audio=True).first()
out_file = song.download()

#Save file format mp3
base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)

#Return Sucess
print(youtube_downloader.title + " Sucess Download")

