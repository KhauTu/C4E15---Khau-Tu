url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
output_file_name = 'VNM_BCTC_4Q.xlsx'

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

# 1 Download website
data = urlopen(url).read()
html_content = data.decode('utf-8')

html_file = open('VNM_cafef.html', 'wb') # write
html_file.write(data)
html_file.close()

# 2 Extract ROI (Region of interest)

soup = BeautifulSoup(html_content, 'html.parser')
# table = soup.find_all('table')
table = soup.find('table',id = 'tableContent')

# row_list = table[3].find_all('tr')
row_list = table.find_all('tr')
# print(row_list[0])
tab_data = []
for k, row in enumerate(row_list):
    if k % 3 == 0:
        td = row_list[k].find_all('td')
        item = td[0].string
        Q4_16 = td[1].string
        Q1_17 = td[2].string
        Q2_17 = td[3].string
        Q3_17 = td[4].string
        one_row = {
        'item': item,
        'Q4_16': Q4_16,
        'Q1_17': Q1_17,
        'Q2_17': Q2_17,
        'Q3_17': Q3_17
        }
        tab_data.append(one_row)
    else:
        pass

# 3 Extract News
# print(tab_data)
pyexcel.save_as(records = tab_data, dest_file_name = 'VNM_BCTC_4Q.xlsx')
