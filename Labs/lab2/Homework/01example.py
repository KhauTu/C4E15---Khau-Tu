from __future__ import unicode_literals
import youtube_dl
id = 0
ydl_opts = {
    'outtmpl': '%(title)s-%(id)s.%(ext)s'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
