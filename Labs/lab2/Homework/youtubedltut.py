# pip install youtube-dl
from youtube_dl import YoutubeDL

# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=4fQRYA74zZg']) # Remember to put your video in a list, eventhough one video is downloaded

# Sample 2: Download multiple youtube videos
dl = YoutubeDL()
# Put list of song url in download function to download them, one by one
dl.download(['https://www.youtube.com/watch?v=Q04JP_sA174', 'https://www.youtube.com/watch?v=nqOs4kwF3qY'])

# Sample 3: Download audio
options = {
    'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=q11RwNuKfV8'])

# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (video)
}
dl=YoutubeDL(options)
dl.download(['nỗi nhớ kéo dài'])

# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['cơ hội đánh rơi'])
