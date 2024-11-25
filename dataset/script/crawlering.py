'''
무직전생 일본어 판
에리스 나오는 부분을 크롤링해서 저장하는 코드
'''
import requests
from bs4 import BeautifulSoup
for chapter in range(13,65):
    url = "https://ncode.syosetu.com/n9669bk/"+str(chapter)+"/"

    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    novel_body = soup.find("div", class_="p-novel__body")
    if novel_body:
        print("Novel Chapter {0} Found!".format(chapter))
        f=open("chapter_{0}.txt".format(chapter),"w",encoding="utf-8")
        f.write(novel_body.text.strip())
        f.close()
    else:
        print("Novel Chapter {0} Not Found.".format(chapter))

