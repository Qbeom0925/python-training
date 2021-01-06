import requests
from bs4 import BeautifulSoup

html=requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8')

soup=BeautifulSoup(html.text, 'html.parser')

#'div' 태그명과 class 'weather_box'
data1 = soup.find('div',{'class':'weather_box'})
find_add=data1.find('span',{'class': 'btn_select'}).text
print(find_add)

find_currenttemp=data1.find('span',{'class': 'todaytemp'}).text
print('현재온도: '+find_currenttemp+'℃')