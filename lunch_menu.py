import requests
from bs4 import BeautifulSoup

url = 'https://school.cbe.go.kr/chungju-m/M010313/list'                                                                             #target URL

response = requests.get(url)                                                                                                        #Get target's HTML code

if response.status_code == 200:                                                                                                     #If GET request is success
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.select_one('#usm-content-body-id > ul > li:nth-child(1)')                                                           #Get date
    lunch_menu = soup.select_one('#usm-content-body-id > ul.tch-lnc-list > li.tch-lnc-wrap > dl > dd.tch-lnc > ul')                 #Get menu
    if lunch_menu == None:                                                                                                          #If menu is not exist
        lunch_menu = '\n식단이 없습니다.\n'
        crawled_data = date.get_text() + '\n' + lunch_menu

    else:
        crawled_data = date.get_text() + '\n' + lunch_menu.get_text()                                                               #Merge crawled data and formatting
        
    print(crawled_data)                                                                                                             #Print crawled data

else :                                                                                                                              #If GET request is fail
    print('오류가 발생했습니다.')
