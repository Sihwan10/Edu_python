import requests
from bs4 import BeautifulSoup
import sys

input = sys.argv[1]

# url 주소
url = "https://ko.wikipedia.org/wiki/" + input

# url 접근해 정보 가져오기(requests)
res = requests.get(url)

# 정보 내 필요한 데이터 파싱(BeautifulSoup)
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.find_all('p') # list 형식으로 반환

print(data[0].text)