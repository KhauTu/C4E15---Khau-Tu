url = 'https://www.apple.com/itunes/charts/songs/'
output_file_name = 'itunes_topsong.xlsx'

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

data = urlopen(url).read()
html_content = data.decode('utf-8')

# html_file = open('itunes_topsong.html', 'wb') # write
# html_file.write(data)
# html_file.close()

soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find_all('div', 'section-content')

li_list = div[1].find_all('li')

top_list = []

for li in li_list:
    Name = li.h3.string
    Artist = li.h4.string
    song = {
    'Name': Name,
    'Artist': Artist,
    }
    top_list.append(song)
# print(top_list)
# pyexcel.save_as(records = top_list, dest_file_name = 'itunes_topsong.xlsx')

from youtube_dl import YoutubeDL

download_list = []
stt = 0
for i in top_list:
    down_song = []
    k = i['Name'] + ' ' + i['Artist']
    down_song.append(k)
    # download_list.append(k)
    stt += 1
    print(stt, ": ", k)
# print(download_list)
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1
        # 'outtmpl': '%(title)s-%(id)s.%(ext)s'
    }
    # print(options['outtmpl'])
    dl = YoutubeDL(options)
    dl.download(down_song)
