from bs4 import BeautifulSoup
import requests
import re
import os

url = "http://www.inu.ac.kr/com/cop/mainWork/foodList2.do?siteId=inu&id=inu_050110030000"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, "lxml")
s = soup.find("div", attrs = {"class":"sickdangmenu"})
for corner in s.find_all("dl"):
    print (corner.dd.text[6:])
    os.system('espeak "' + corner.dd.text[6:] + '"')
