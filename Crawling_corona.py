import requests
from bs4 import BeautifulSoup

html = requests.get("https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98")

soup= BeautifulSoup(html.text, 'html.parser')

data1=soup.find('div',{'class':'status_today'})
data2=data1.find('ul')
data3=data2.find('li',{'class','info_02'})
data4=data2.find('li',{'class','info_03'})

find_corona_kr=data3.find('em',{'class':'info_num'}).text
find_corona_fc=data4.find('em',{'class':'info_num'}).text


print("국내발생: "+find_corona_kr)
print("해외유입: "+find_corona_fc)