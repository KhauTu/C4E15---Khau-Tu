url = 'http://dantri.com.vn'
output_file_name = 'news.xlsx'

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
# # 1 Download website
# # 1.1 Open a connection
# conn = urlopen(url)
# # 1.2 Read
# data = conn.read()
# # internet error: socket timeout
#
# # 1.3 Decode
# html_content = data.decode('utf-8')
# # print(html_content)

data = urlopen(url).read()
html_content = data.decode('utf-8')

html_file = open('dantri.html', 'wb') # write
html_file.write(data)
html_file.close()
# 2 Extract ROI (Region of interest)

# 3 Extract News

# Create a soup
soup = BeautifulSoup(html_content, 'html.parser') #xml
ul = soup.find('ul', 'ul1 ulnew', ) # find only one, or the first # class id = "" # 1 soup
li_list = ul.find_all('li') # list of [soup]

# for li in li_list:
#     print(li.prettify())
#     print('* ' * 20)

news_list = []

for li in li_list:
# li = li_list[0]
# h4 = li.h4 # li.find('h4') # li.find_all('h4')[0]
# a = h4.a
    a = li.h4.a
    href = url + a['href']
    # title = a['title']
    title = a.string
    news = {
    'Title': title,
    'Link': href
    }
    news_list.append(news)
    # print(title)
    # print(href)
    # print('* ' * 20)
# print(news_list)

pyexcel.save_as(records = news_list, dest_file_name = 'dantri.xlsx')
