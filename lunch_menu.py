from types import NoneType
import requests
from bs4 import BeautifulSoup

url = 'https://school.cbe.go.kr/chungju-m/M010313/list'                                                                             #target URL

response = requests.get(url)                                                                                                        #Get target's HTML code

if response.status_code == 200:                                                                                                     #If GET request is success
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.select_one('#usm-content-body-id > ul > li:nth-child(1)').get_text()                                                #Get date
    lunch_menu = soup.select_one('#usm-content-body-id > ul.tch-lnc-list > li.tch-lnc-wrap > dl > dd.tch-lnc > ul').get_text()      #Get menu
    if lunch_menu == None:                                                                                                          #If menu is not exist
        lunch_menu = '식단이 없습니다.'
    crawled_data = date + '\n' + lunch_menu                                                                                         #Merge crawled data and formatting
    print(crawled_data)                                                                                                             #Print crawled data

else :                                                                                                                              #If GET request is fail
    print('오류가 발생했습니다.')